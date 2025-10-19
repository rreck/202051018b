```json
{
  "id": "71ba6c17d72ad0e1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286590,
  "host_pid": "9e6742732c60:1",
  "hash": "570d47d8eab81fc045948db5661af71a5c6a31d23de55ca95a80d4046ee6de63",
  "cid": "QmV1570d47d8eab81fc045948db5661af71a5c6a31d2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286590,
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
      "evaluated_at": 1760286590
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
  "sig": "e0358bb46f783e0bc2e5d79fd850629082083512d657ac46b5c35fc1b6b29ea8"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 031201467798287
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 13328790, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 29, 'first_seen': 1760285765, 'matching_hash': 'b1c6e5e3cdd02671'}}}