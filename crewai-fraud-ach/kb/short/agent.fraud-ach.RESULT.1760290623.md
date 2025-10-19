```json
{
  "id": "c23f7e5f9c0ec678",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290623,
  "host_pid": "9e6742732c60:1",
  "hash": "3508a4ef9a0424eae0ec1eb6340cfa0b00ecb037ff96c8eeb3e3baf914e92434",
  "cid": "QmV13508a4ef9a0424eae0ec1eb6340cfa0b00ecb037",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290623,
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
      "evaluated_at": 1760290623
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
  "sig": "d28cfaeb50c71d72bd40e6b97b086e4f4ce78cc203eedddfc7bf0bf19aeaa80d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271109324
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 155, 'threshold': 50, 'total_amount': 38750000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 154, 'first_seen': 1760285764, 'matching_hash': '28f72b559ab32ea0'}}}unt_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}