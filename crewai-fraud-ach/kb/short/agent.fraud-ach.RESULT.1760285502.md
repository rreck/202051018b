```json
{
  "id": "3b5e89760a7dc565",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285502,
  "host_pid": "9e6742732c60:1",
  "hash": "f1c475977b396dd28d17582ec34f73ecdded44ab76cc83a41a0a32be36c5fa81",
  "cid": "QmV1f1c475977b396dd28d17582ec34f73ecdded44ab",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285502,
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
      "evaluated_at": 1760285502
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
  "sig": "07141e372f909d957d54ab729e89fd3f9370705f9f1b6bb43900d3b8306f8fe4"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000026203898
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 52, 'threshold': 50, 'total_amount': 21912488, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 51, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}