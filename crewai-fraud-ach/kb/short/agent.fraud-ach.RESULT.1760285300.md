```json
{
  "id": "f723829b6678888a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285300,
  "host_pid": "9e6742732c60:1",
  "hash": "3d34e87c92c79fc7a920342a4708699789547ba6d2c2ea7f561b770af76975fa",
  "cid": "QmV13d34e87c92c79fc7a920342a4708699789547ba6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285300,
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
      "evaluated_at": 1760285300
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "356f442ff49578f397bb41ab4972175865bf2996f399675f1ab63f8c5210ae63"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000026203898
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 13484608, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 31, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}