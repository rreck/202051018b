```json
{
  "id": "4d306179dbd1eeb6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288722,
  "host_pid": "9e6742732c60:1",
  "hash": "8b31f46c5551fdecfb9465b9b28914676a36a91376222edefabdbbe2a24911d4",
  "cid": "QmV18b31f46c5551fdecfb9465b9b28914676a36a913",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288722,
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
      "evaluated_at": 1760288722
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
  "sig": "ba42b023f22c5b860a72199d8ae48655f80191223cc751657cd507b25ed0214e"
}
```

Fraud detected: amount_anomaly (score: 89)
Transaction: 111000020782458
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 102, 'threshold': 50, 'total_amount': 876762624, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 101, 'first_seen': 1760285764, 'matching_hash': '09f46afbb4d14766'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 84, 'details': {'zscore': 4.48, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 8595712}}}