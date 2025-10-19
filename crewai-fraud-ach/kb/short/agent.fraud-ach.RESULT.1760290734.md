```json
{
  "id": "6662a3a651cbe1e6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290734,
  "host_pid": "9e6742732c60:1",
  "hash": "5deaf3ff22a53eb3637a13b12e243ba8630473b7e0686890dd467713bbd5711e",
  "cid": "QmV15deaf3ff22a53eb3637a13b12e243ba8630473b7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290734,
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
      "evaluated_at": 1760290734
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
  "sig": "ef6b0daa06ab91f008838c988cf92e2ae4c4c74bfff6237bda33701fdc20b442"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000027419247
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 158, 'threshold': 50, 'total_amount': 74231718, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 157, 'first_seen': 1760285763, 'matching_hash': 'f49fdb64c00c5aec'}}}maly': {'fraud_detected': True, 'risk_score': 80, 'details': {'zscore': 4.06, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 7854285}}}