```json
{
  "id": "a333f2a6454828fd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293406,
  "host_pid": "9e6742732c60:1",
  "hash": "733e887bfcb3576822f40fbd9c52f961b536e0feaf52a7e3b89a3c26c0999947",
  "cid": "QmV1733e887bfcb3576822f40fbd9c52f961b536e0fe",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293406,
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
      "evaluated_at": 1760293406
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
  "sig": "2e9584af4fedc448e6ac7750a7c9ffa92ad385d52dc0ad65232ccae014e47da9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000036798243
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 218, 'threshold': 50, 'total_amount': 96376056, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 217, 'first_seen': 1760285763, 'matching_hash': '9f3869b775bbb8aa'}}}maly': {'fraud_detected': True, 'risk_score': 79, 'details': {'zscore': 3.93, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 7623976}}}