```json
{
  "id": "8c9274c1b9a04751",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291306,
  "host_pid": "9e6742732c60:1",
  "hash": "8ab52537415b5c90e546e00148900dda12be2d321901675571808504e2c79088",
  "cid": "QmV18ab52537415b5c90e546e00148900dda12be2d32",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291306,
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
      "evaluated_at": 1760291306
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
  "sig": "350c859b709aadf2102e9ce8d3de34900c25e41b1f1ee81242badeedaf99e946"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026545394
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 172, 'threshold': 50, 'total_amount': 52321024, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 171, 'first_seen': 1760285763, 'matching_hash': '1ef68d78d8cabe5b'}}}maly': {'fraud_detected': True, 'risk_score': 79, 'details': {'zscore': 3.93, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 7623976}}}