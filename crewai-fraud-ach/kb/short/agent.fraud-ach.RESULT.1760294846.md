```json
{
  "id": "ac5d7a3949f68f24",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294846,
  "host_pid": "9e6742732c60:1",
  "hash": "e0834cf962d86d18a8d6d09f82ca8821fedf3e8bf3ca96b1fe7ca88926ea3f74",
  "cid": "QmV1e0834cf962d86d18a8d6d09f82ca8821fedf3e8b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294846,
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
      "evaluated_at": 1760294846
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "amount_anomaly",
    "risk_critical"
  ],
  "sig": "6254f52b9aecbb531df2777a04f931e469a310340f1353b79ed08fe928362b1b"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 111000028976117
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 245, 'threshold': 50, 'total_amount': 1458147635, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 244, 'first_seen': 1760285765, 'matching_hash': 'f0572624c8eaf0e8'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 5951623}}}