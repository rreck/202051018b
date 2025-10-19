```json
{
  "id": "bdf9d0027733fc1f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291135,
  "host_pid": "9e6742732c60:1",
  "hash": "c85ce9301b3978496ee0da9e77c8ca739bfe77a542f100bcc5dfe774d63c03ac",
  "cid": "QmV1c85ce9301b3978496ee0da9e77c8ca739bfe77a5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291135,
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
      "evaluated_at": 1760291135
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
  "sig": "364aa766a3bf680d49751dad210bfbf3975c3a2d5b7660dcf8180472bcfc0dab"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154236496
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 168, 'threshold': 50, 'total_amount': 60841872, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 167, 'first_seen': 1760285763, 'matching_hash': '2022d9adcee53cdf'}}}maly': {'fraud_detected': True, 'risk_score': 73, 'details': {'zscore': 3.38, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 6664302}}}