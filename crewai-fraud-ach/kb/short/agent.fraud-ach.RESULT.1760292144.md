```json
{
  "id": "13a13737f7aebe61",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292144,
  "host_pid": "9e6742732c60:1",
  "hash": "8f2104fee0241e29503e445222f17e874f0a76dda21be13cc900857ba848a271",
  "cid": "QmV18f2104fee0241e29503e445222f17e874f0a76dd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292144,
      "method": "automated_fraud_detection",
      "vc_type": "VerifiableCredential"
    },
    "ucon": {
      "usage_constraints": [
        "no_pii_export",
        "audit_required"
      ],
      "purpose": "fraud_detection_analysis",
      "enforcement": "mandatory"
    },
    "eval": {
      "confidence": 1.0,
      "evidence_count": 0,
      "review_status": "pending",
      "evaluated_at": 1760292144
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "2eeb66616744cc918a54d20eb718e02bee9df1a3323d01d48854f1a6f3564658"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009595535562
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 191, 'threshold': 50, 'total_amount': 25822627, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 190, 'first_seen': 1760285763, 'matching_hash': '052e7693e8a3f40d'}}}