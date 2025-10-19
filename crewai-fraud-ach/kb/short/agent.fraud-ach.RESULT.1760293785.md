```json
{
  "id": "f44bb46fc1cc613d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293785,
  "host_pid": "9e6742732c60:1",
  "hash": "5cd8cd8609a1ab71299c8f3ec5b10b9c0aa15ba70c68116666f8723fd2625270",
  "cid": "QmV15cd8cd8609a1ab71299c8f3ec5b10b9c0aa15ba7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293785,
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
      "evaluated_at": 1760293785
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
  "sig": "9ffd1a04e9dd35d9f4d2b64f2f7cedea80d560c9908f8bcb583b5e5cda526e1e"
}
```

Fraud detected: amount_anomaly (score: 89)
Transaction: 121000241325245
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 225, 'threshold': 50, 'total_amount': 1835922375, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 224, 'first_seen': 1760285765, 'matching_hash': '97920a0a35eda98b'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 82, 'details': {'zscore': 4.23, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 8159655}}}