```json
{
  "id": "800ddc371da712c3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292702,
  "host_pid": "9e6742732c60:1",
  "hash": "24ea92ad1d7c4487f387e7d91bcba90bd13af501f6c81993e2a240021e9ad287",
  "cid": "QmV124ea92ad1d7c4487f387e7d91bcba90bd13af501",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292702,
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
      "evaluated_at": 1760292702
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
  "sig": "e8717aebfa75ed4fbd2508eb779e99a8bf2b148dc77f204fa81e7dabe3e9e669"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000020380567
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 203, 'threshold': 50, 'total_amount': 57336741, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 202, 'first_seen': 1760285764, 'matching_hash': 'ee2651561ec204b1'}}}