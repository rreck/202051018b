```json
{
  "id": "5df6b49097fd3963",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292148,
  "host_pid": "9e6742732c60:1",
  "hash": "27417538f97e33ae634c4a1cb8038253b14d85d9294c26bdfc22d2e817581c9a",
  "cid": "QmV127417538f97e33ae634c4a1cb8038253b14d85d9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292148,
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
      "evaluated_at": 1760292148
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
  "sig": "2adb94d1268073c3c56121cabae7b655b7fae1f113faba95e944a823d93d9f30"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000030798175
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 267, 'threshold': 50, 'total_amount': 31797564, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 266, 'first_seen': 1760284979, 'matching_hash': 'fdbb68f6e232305a'}}}