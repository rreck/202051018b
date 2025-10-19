```json
{
  "id": "e85dd64c626ea861",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290355,
  "host_pid": "9e6742732c60:1",
  "hash": "c276f71a69ddf738d26c6ccb9d439316f0992c348a98639fb9c25a91c63bece6",
  "cid": "QmV1c276f71a69ddf738d26c6ccb9d439316f0992c34",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290355,
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
      "evaluated_at": 1760290355
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
  "sig": "40e7439accd4bc58e5bdb92ccd847d17ef80b76eedd428ee329abb572d4b0cbc"
}
```

Fraud detected: amount_anomaly (score: 88)
Transaction: 044000034245036
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 148, 'threshold': 50, 'total_amount': 1145997744, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 147, 'first_seen': 1760285764, 'matching_hash': '2d29d6825e083497'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 79, 'details': {'zscore': 4.0, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 7743228}}}