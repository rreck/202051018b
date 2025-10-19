```json
{
  "id": "c396a92999587ebd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292462,
  "host_pid": "9e6742732c60:1",
  "hash": "d86c1a4d0ddf2398687700d29babe49154a5e359c3f392d65a89605fa94c2b0f",
  "cid": "QmV1d86c1a4d0ddf2398687700d29babe49154a5e359",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292462,
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
      "evaluated_at": 1760292462
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
  "sig": "8af5db332978d89eed918cf36e3076405c6473c378482a6da7b422c461a0463e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026959997
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 198, 'threshold': 50, 'total_amount': 44971542, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 197, 'first_seen': 1760285764, 'matching_hash': '4bd6adbc5f3cfca3'}}}