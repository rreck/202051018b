```json
{
  "id": "d92653c96ee22159",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292311,
  "host_pid": "9e6742732c60:1",
  "hash": "21e75394cfb3a8aea5e05168e7da101be8b7f86847b51993e0f61b47563f7073",
  "cid": "QmV121e75394cfb3a8aea5e05168e7da101be8b7f868",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292311,
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
      "evaluated_at": 1760292311
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
  "sig": "da219c9376a0caed52ef8a3d94792ef97724fbb6940c07e3dada5f598f22b821"
}
```

Fraud detected: amount_anomaly (score: 86)
Transaction: 026009599754451
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 195, 'threshold': 50, 'total_amount': 1299538890, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 194, 'first_seen': 1760285763, 'matching_hash': '546a5bdf8e1b6fa5'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 73, 'details': {'zscore': 3.38, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 6664302}}}