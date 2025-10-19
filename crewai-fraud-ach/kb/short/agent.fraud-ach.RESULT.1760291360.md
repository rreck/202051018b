```json
{
  "id": "7d9e5a163b82283d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291360,
  "host_pid": "9e6742732c60:1",
  "hash": "45a295a939f6eeaa5aa07506810f2189fd25d5d96d9683024d48b0fb428219f6",
  "cid": "QmV145a295a939f6eeaa5aa07506810f2189fd25d5d9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291360,
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
      "evaluated_at": 1760291360
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
  "sig": "361a416c6fcf1d7ee80a8855e6e8ac73983d53355c61b82403e97a4acd76f473"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009590010204
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 173, 'threshold': 50, 'total_amount': 80161453, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 172, 'first_seen': 1760285763, 'matching_hash': 'd097f3de33be356c'}}}