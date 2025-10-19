```json
{
  "id": "aa03466e3a6adf87",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286524,
  "host_pid": "9e6742732c60:1",
  "hash": "ce6abeaf5318e38d24623bb42c0dca12af038386973f5831a0cf5405c6575e45",
  "cid": "QmV1ce6abeaf5318e38d24623bb42c0dca12af038386",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286524,
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
      "evaluated_at": 1760286524
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
  "sig": "c8e4215eec74a5295f62036674c5a793034ad048a8f9cb24fa39fb8b8e15f8f3"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000029769834
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 10767540, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 27, 'first_seen': 1760285764, 'matching_hash': '4022d05a51a758f8'}}}760284979, 'matching_hash': 'af51af40be20c608'}}}