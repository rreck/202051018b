```json
{
  "id": "be43f58c54ac7bb8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287390,
  "host_pid": "9e6742732c60:1",
  "hash": "c5dc236e48bc11204823514571d48b50ccc1ec62eacd1b1df9e61f61d97f95ba",
  "cid": "QmV1c5dc236e48bc11204823514571d48b50ccc1ec62",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287390,
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
      "evaluated_at": 1760287390
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
  "sig": "68861417f64ef43b04d4aec913016afa592e6af169d696fbac9c4c7d69cd0a79"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 044000035430994
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 58, 'threshold': 50, 'total_amount': 24638400, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 57, 'first_seen': 1760285765, 'matching_hash': '24f97a880bb92d0e'}}}