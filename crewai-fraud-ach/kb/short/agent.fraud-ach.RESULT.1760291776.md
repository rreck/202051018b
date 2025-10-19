```json
{
  "id": "e2697ebed92f1871",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291776,
  "host_pid": "9e6742732c60:1",
  "hash": "071acf11ea3b59cdbca2637dc7ab4268c5e390fdd68ec194232b7c97a98a0905",
  "cid": "QmV1071acf11ea3b59cdbca2637dc7ab4268c5e390fd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291776,
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
      "evaluated_at": 1760291776
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
  "sig": "11335bd6b7bf02bc2f39ff06ab12505f17710c73379f58de80ec2d9c0a0358bf"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469258561
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 183, 'threshold': 50, 'total_amount': 47532603, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 182, 'first_seen': 1760285763, 'matching_hash': 'c5dbb685e09199e5'}}}