```json
{
  "id": "a1e1019648004202",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293019,
  "host_pid": "9e6742732c60:1",
  "hash": "25a0add7fb554819e43aa1628bce7152bc8886982ab7f8baa819994baa7a7bb6",
  "cid": "QmV125a0add7fb554819e43aa1628bce7152bc888698",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293019,
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
      "evaluated_at": 1760293019
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
  "sig": "7e3f5b9752514a468ffbae3ab3d92f809cefefe5e2429d20595e1ff0b555f1c6"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 111000027318988
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 210, 'threshold': 50, 'total_amount': 1057447860, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 209, 'first_seen': 1760285763, 'matching_hash': '9c4bf7694cd7e546'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 5035466}}}