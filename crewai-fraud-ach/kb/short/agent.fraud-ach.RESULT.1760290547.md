```json
{
  "id": "bd3df3578721697c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290547,
  "host_pid": "9e6742732c60:1",
  "hash": "89d0ea55d625125512db0b17af5e4bc9f1c4d07737aa79e6b03cff1989d678b3",
  "cid": "QmV189d0ea55d625125512db0b17af5e4bc9f1c4d077",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290547,
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
      "evaluated_at": 1760290547
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
  "sig": "a23543baf2ced38a35eced8b56567952a7fab3c2643ea533d531b9d725803fa1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009595571766
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 153, 'threshold': 50, 'total_amount': 75211587, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 152, 'first_seen': 1760285763, 'matching_hash': '7b9b43f48a0de4d3'}}}unt_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}