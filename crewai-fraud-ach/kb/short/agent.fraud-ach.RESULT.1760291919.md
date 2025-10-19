```json
{
  "id": "ed1e9dc5d66ab8ec",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291919,
  "host_pid": "9e6742732c60:1",
  "hash": "776d0b5137f09305fda49a6167f7739cd7c31d8a24d01c09a8fa40fcfb83deb1",
  "cid": "QmV1776d0b5137f09305fda49a6167f7739cd7c31d8a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291919,
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
      "evaluated_at": 1760291919
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
  "sig": "0db51d85a1a65c440cd290f2d9fa3a576f812259e618a9a17471151219cedba5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201468629827
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 186, 'threshold': 50, 'total_amount': 16442772, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 185, 'first_seen': 1760285763, 'matching_hash': 'f998250ed7d87b2f'}}}