```json
{
  "id": "c2cc905ecaa5f70b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287700,
  "host_pid": "9e6742732c60:1",
  "hash": "d19e0c31840f25f6aed4067f3a7c8f9b79e512b5c5c313b7c190e835831b3b87",
  "cid": "QmV1d19e0c31840f25f6aed4067f3a7c8f9b79e512b5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287700,
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
      "evaluated_at": 1760287700
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
  "sig": "efc94b5456a580279b9c6f9046dd26b1f826d17869dc104bbf1428a420dd7285"
}
```

Fraud detected: amount_anomaly (score: 82)
Transaction: 063100275758456
Details: {'velocity': {'fraud_detected': True, 'risk_score': 88, 'details': {'transaction_count': 69, 'threshold': 50, 'total_amount': 649783281, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 68, 'first_seen': 1760285765, 'matching_hash': 'e3feb2a34db32d71'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 75, 'details': {'zscore': 3.58, 'mean': 1373847.7, 'stdev': 2245589.6016213675, 'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 9417149}}}