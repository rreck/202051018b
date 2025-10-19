```json
{
  "id": "b025a6ec7d3a5a79",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291222,
  "host_pid": "9e6742732c60:1",
  "hash": "da8dcf43f762fcc25de896c263add064eb9ea629d348fbb674be2cec162c75ba",
  "cid": "QmV1da8dcf43f762fcc25de896c263add064eb9ea629",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291222,
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
      "evaluated_at": 1760291222
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
  "sig": "06f1e45c4b98ed74f63f6856340cc821980ecf73b53c8b47947d7147f7d944ea"
}
```

Fraud detected: amount_anomaly (score: 89)
Transaction: 111000028341368
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 170, 'threshold': 50, 'total_amount': 1452221260, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 169, 'first_seen': 1760285763, 'matching_hash': 'b11d2debe374bbec'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 84, 'details': {'zscore': 4.45, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 8542478}}}