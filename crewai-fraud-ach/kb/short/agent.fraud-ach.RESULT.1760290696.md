```json
{
  "id": "d17e8de6522c4621",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290696,
  "host_pid": "9e6742732c60:1",
  "hash": "0b915dfa139b6d88a954be0bf7656df3492245d92e1346d8790b25f2d90492be",
  "cid": "QmV10b915dfa139b6d88a954be0bf7656df3492245d9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290696,
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
      "evaluated_at": 1760290696
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
  "sig": "07392f7c5af8f0e5fbda41842719003eb3e9e24cf9a75fad77c12fc92deb7610"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105151540950
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 157, 'threshold': 50, 'total_amount': 30356264, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 156, 'first_seen': 1760285763, 'matching_hash': '9c022c6e80e7fcd3'}}}maly': {'fraud_detected': True, 'risk_score': 89, 'details': {'zscore': 4.94, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 9410889}}}