```json
{
  "id": "86f278518fa8759a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291697,
  "host_pid": "9e6742732c60:1",
  "hash": "7c5e1c8e6b1679419c761f0110fd8308bb472b140dd6ea382834bb49275e204c",
  "cid": "QmV17c5e1c8e6b1679419c761f0110fd8308bb472b14",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291697,
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
      "evaluated_at": 1760291697
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
  "sig": "b3afadd7bc2cbe57a0203fc4753474b447723e540fa00a951bf09dcf3d5c50d3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242260871
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 181, 'threshold': 50, 'total_amount': 60245126, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 180, 'first_seen': 1760285764, 'matching_hash': '677d45847b06d7dd'}}}