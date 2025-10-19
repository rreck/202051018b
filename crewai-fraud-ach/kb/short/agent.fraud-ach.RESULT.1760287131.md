```json
{
  "id": "9fe6c5e78658fd25",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287131,
  "host_pid": "9e6742732c60:1",
  "hash": "ef7339ba9911c4cc0d31cb86be07edbf950796346f6f20a8b41f429b680e33ba",
  "cid": "QmV1ef7339ba9911c4cc0d31cb86be07edbf95079634",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287131,
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
      "evaluated_at": 1760287131
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
  "sig": "b263402d765444d43d71335f777130204fb8a3c4d2421c472496d2d89844c07e"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 063100274472610
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 16117178, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 48, 'first_seen': 1760285764, 'matching_hash': '7db40904e20d1f88'}}}