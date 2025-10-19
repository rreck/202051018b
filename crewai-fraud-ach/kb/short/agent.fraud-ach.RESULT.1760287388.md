```json
{
  "id": "02252a22ff68a84e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287388,
  "host_pid": "9e6742732c60:1",
  "hash": "f59d4e9e539d1984d1aaa55a1b814b9ebb7984ee94079edb7afc675b4a5a129e",
  "cid": "QmV1f59d4e9e539d1984d1aaa55a1b814b9ebb7984ee",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287388,
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
      "evaluated_at": 1760287388
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
  "sig": "e19aa75c44ae3139d0ca82e55d11a33ee4bcd2b310c9f8beba743524eb8cce76"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000025839448
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 58, 'threshold': 50, 'total_amount': 21948766, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 57, 'first_seen': 1760285765, 'matching_hash': 'a0edb6bd92ae1076'}}}