```json
{
  "id": "2f68c58a55c9387b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293420,
  "host_pid": "9e6742732c60:1",
  "hash": "032d6dcdb184dc49987e171c58e25c66ebbcf39e438dd61a6fbc18a97d365fb2",
  "cid": "QmV1032d6dcdb184dc49987e171c58e25c66ebbcf39e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293420,
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
      "evaluated_at": 1760293420
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "round_amount_pattern",
    "risk_high"
  ],
  "sig": "4cabce9cac6d6799f3a041353934150ec55a874e0f278e9d19e0c0a67aba18dd"
}
```

Fraud detected: round_amount_pattern (score: 71)
Transaction: 122105158962917
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 218, 'threshold': 50, 'total_amount': 218000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 217, 'first_seen': 1760285763, 'matching_hash': '11dc2cfd2eb8ef5d'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}