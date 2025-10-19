```json
{
  "id": "ef442e37ac67e794",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286527,
  "host_pid": "9e6742732c60:1",
  "hash": "077fae280afc521988bb79d1e313c6e1c612e3d7d2a72c063f1aa651395f1441",
  "cid": "QmV1077fae280afc521988bb79d1e313c6e1c612e3d7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286527,
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
      "evaluated_at": 1760286527
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
  "sig": "20c39e33b09b4a22240cc1dd4fb94085409672882d17f1d1aef901082fbb5166"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 063100279280277
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 12368300, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 27, 'first_seen': 1760285763, 'matching_hash': '5e64cdd29eaed333'}}}