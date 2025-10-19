```json
{
  "id": "936896daaa00b9ac",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287019,
  "host_pid": "9e6742732c60:1",
  "hash": "54fdca5a1d03ae0633c5aa2b509a37d8cd53a31b99cc2c3ec74fa571927339d0",
  "cid": "QmV154fdca5a1d03ae0633c5aa2b509a37d8cd53a31b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287019,
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
      "evaluated_at": 1760287019
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
  "sig": "92ccce8efcfb79f23e92768b29579c325ca93ab04c63928da86ec08d1f074b04"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 121000243187094
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 20177775, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 44, 'first_seen': 1760285764, 'matching_hash': '46900333a68fa7ba'}}}