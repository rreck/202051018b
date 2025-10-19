```json
{
  "id": "83fd13ea7d77fb47",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287986,
  "host_pid": "9e6742732c60:1",
  "hash": "22c7fd0ae5f897c54425e6724007e866ca40fa1b9ca83c0b3f84bec4ecfc7d74",
  "cid": "QmV122c7fd0ae5f897c54425e6724007e866ca40fa1b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287986,
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
      "evaluated_at": 1760287986
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
  "sig": "750d69665983c496cf6e34d5ba7c9d61c8a00d8d452d4f027b32ff80002e840e"
}
```

Fraud detected: amount_anomaly (score: 85)
Transaction: 111000028341368
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 79, 'threshold': 50, 'total_amount': 674855762, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 78, 'first_seen': 1760285763, 'matching_hash': 'b11d2debe374bbec'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 71, 'details': {'zscore': 3.19, 'mean': 1373847.7, 'stdev': 2245589.6016213675, 'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 8542478}}}