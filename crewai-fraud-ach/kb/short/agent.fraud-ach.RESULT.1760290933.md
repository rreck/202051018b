```json
{
  "id": "1636c3a3cd39b761",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290933,
  "host_pid": "9e6742732c60:1",
  "hash": "d7f712aba591116163c4a9ea891ea6dceef98f30ceaef3555409929384119fe8",
  "cid": "QmV1d7f712aba591116163c4a9ea891ea6dceef98f30",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290933,
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
      "evaluated_at": 1760290933
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
  "sig": "fa0c4eaafa734bd893fb3204fbd70aa4d3f7d92190cf9afb3d6acf482c110304"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000022225777
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 163, 'threshold': 50, 'total_amount': 13237719, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 162, 'first_seen': 1760285763, 'matching_hash': '9e191c483430cef0'}}}maly': {'fraud_detected': True, 'risk_score': 92, 'details': {'zscore': 5.25, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 9947388}}}