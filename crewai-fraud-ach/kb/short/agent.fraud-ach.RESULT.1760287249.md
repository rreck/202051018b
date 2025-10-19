```json
{
  "id": "9d19cea19ed1a6a8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287249,
  "host_pid": "9e6742732c60:1",
  "hash": "e323130c47d02d247276533d5af563c99a41afe2e7bedc8d3709152ce7c458bd",
  "cid": "QmV1e323130c47d02d247276533d5af563c99a41afe2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287249,
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
      "evaluated_at": 1760287249
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
  "sig": "a95bfd1be1da7077fc0afabd36c08fe212d65abb84eb676e174ec64a52577286"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 044000038099532
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 53, 'threshold': 50, 'total_amount': 21275366, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 52, 'first_seen': 1760285765, 'matching_hash': 'ac68ba9e81a65c72'}}}