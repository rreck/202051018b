```json
{
  "id": "51a342d49320313f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287043,
  "host_pid": "9e6742732c60:1",
  "hash": "d5b714087930195761df4ab7969a9e6dd8fd65ea71496392737bbb7fe1c1a7f8",
  "cid": "QmV1d5b714087930195761df4ab7969a9e6dd8fd65ea",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287043,
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
      "evaluated_at": 1760287043
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
  "sig": "c38100aa63e255dd3312187d6370d175b2eac9f2c242fd49fe82f97388ea7393"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105150565846
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 22814620, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 45, 'first_seen': 1760285765, 'matching_hash': 'c006c1a99d006ad8'}}}760284979, 'matching_hash': 'aab4f056297a675d'}}}