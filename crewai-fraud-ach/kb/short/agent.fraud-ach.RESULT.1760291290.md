```json
{
  "id": "0ebcaea4e410fbc8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291290,
  "host_pid": "9e6742732c60:1",
  "hash": "a98f35b47bf606f817be1488d01d357311dd610dc7b58dded2f93d4bd8ac2cdf",
  "cid": "QmV1a98f35b47bf606f817be1488d01d357311dd610d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291290,
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
      "evaluated_at": 1760291290
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
  "sig": "105470722ba3e219a0e5afb315d002df7dbfefde3bf3794c64280305e339ed26"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 031201465841026
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 171, 'threshold': 50, 'total_amount': 85500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 170, 'first_seen': 1760285765, 'matching_hash': 'e2a83dab91a99cc0'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}