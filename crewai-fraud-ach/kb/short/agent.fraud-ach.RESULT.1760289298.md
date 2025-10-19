```json
{
  "id": "2fa6b0bc15a3cc39",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289298,
  "host_pid": "9e6742732c60:1",
  "hash": "7094c91e48b2fa70c61bc25227f1ebb28acdf05e588614040e1d39d36d2e8970",
  "cid": "QmV17094c91e48b2fa70c61bc25227f1ebb28acdf05e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289298,
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
      "evaluated_at": 1760289298
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
  "sig": "e5cea296db43edaff50670c145eb393fc911c5da0dee80edd7c3a16df1d3bdd7"
}
```

Fraud detected: amount_anomaly (score: 89)
Transaction: 026009592955504
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 119, 'threshold': 50, 'total_amount': 1017364796, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 118, 'first_seen': 1760285765, 'matching_hash': 'e4b1ef1aea3a67a1'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 84, 'details': {'zscore': 4.45, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 8549284}}}