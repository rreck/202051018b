```json
{
  "id": "a391e625d87a74d8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287717,
  "host_pid": "9e6742732c60:1",
  "hash": "90f7b0ce948adac901876621e98128ea23fca3118d005e2fd01f12d15312e2d6",
  "cid": "QmV190f7b0ce948adac901876621e98128ea23fca311",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287717,
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
      "evaluated_at": 1760287717
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "amount_anomaly",
    "risk_high"
  ],
  "sig": "70718bc69a306a4e49839ebc9c70028a7a8a357f755775b2dc04710e01b3d28f"
}
```

Fraud detected: amount_anomaly (score: 78)
Transaction: 044000036587475
Details: {'velocity': {'fraud_detected': True, 'risk_score': 90, 'details': {'transaction_count': 70, 'threshold': 50, 'total_amount': 538643560, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 69, 'first_seen': 1760285763, 'matching_hash': '7583721e7662209c'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 7694908}}}