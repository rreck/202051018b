```json
{
  "id": "a7ed6f2fba0367b8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289893,
  "host_pid": "9e6742732c60:1",
  "hash": "63ff16e6c2558d88c8551ac6a473ce8d53de20a39f77841adbf5acfe5b2a60bb",
  "cid": "QmV163ff16e6c2558d88c8551ac6a473ce8d53de20a3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289893,
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
      "evaluated_at": 1760289893
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
  "sig": "273db1dadcd8e28002e325887ac7756faadc5f6dc94b732056cdd686f7f8e275"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000039510138
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 136, 'threshold': 50, 'total_amount': 15262600, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 135, 'first_seen': 1760285763, 'matching_hash': '4238a333ed8712d2'}}}maly': {'fraud_detected': True, 'risk_score': 78, 'details': {'zscore': 3.85, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 7493680}}}