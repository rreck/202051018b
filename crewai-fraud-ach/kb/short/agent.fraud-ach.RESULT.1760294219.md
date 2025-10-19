```json
{
  "id": "44dabb7a96a4e20c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294219,
  "host_pid": "9e6742732c60:1",
  "hash": "b4f307383ea63278f1bc1caffddcb7b2985f3ccf665d8ddea4e5dd5e098b1ddd",
  "cid": "QmV1b4f307383ea63278f1bc1caffddcb7b2985f3ccf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294219,
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
      "evaluated_at": 1760294219
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
  "sig": "0bc4a6a9bf388c397111b2bf2ba34f94e94e59a7cba30bed49e1ea84bb6a14e7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201462075291
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 234, 'threshold': 50, 'total_amount': 73929726, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 233, 'first_seen': 1760285763, 'matching_hash': '75f7f0ceec197518'}}}}