```json
{
  "id": "f4c0316dc01c85de",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288750,
  "host_pid": "9e6742732c60:1",
  "hash": "2e6090134718a938e1f54e4b15da5f96f2df649eb8b1e8a1ff9dee291e25a994",
  "cid": "QmV12e6090134718a938e1f54e4b15da5f96f2df649e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288750,
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
      "evaluated_at": 1760288750
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
  "sig": "af5813158935214769bf0317ae255a2e69ebd4ee897bd6ffd45936e969ce60b9"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 111000023922367
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 103, 'threshold': 50, 'total_amount': 613510127, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 102, 'first_seen': 1760285763, 'matching_hash': '420dc08dc8ad4808'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 5956409}}}