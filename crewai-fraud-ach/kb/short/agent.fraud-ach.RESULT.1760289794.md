```json
{
  "id": "316acd87e48f6b59",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289794,
  "host_pid": "9e6742732c60:1",
  "hash": "29932339e14ae9f5259ebd85f9c2381a9db077caf6202caba515eb24e1117c30",
  "cid": "QmV129932339e14ae9f5259ebd85f9c2381a9db077ca",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289794,
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
      "evaluated_at": 1760289794
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "f4136761fb0c554a25754ca42eaf6cb2317dbb5729c8c3b9e0cc7bec65e98204"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105155376461
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 133, 'threshold': 50, 'total_amount': 40018503, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 132, 'first_seen': 1760285765, 'matching_hash': 'ed3a1cd9da35e724'}}}maly': {'fraud_detected': True, 'risk_score': 91, 'details': {'zscore': 5.16, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 9795510}}}