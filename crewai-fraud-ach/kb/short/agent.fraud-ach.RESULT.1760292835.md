```json
{
  "id": "9da5a55dc14ac326",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292835,
  "host_pid": "9e6742732c60:1",
  "hash": "8c7c2ad91a567c16e3aab21d5cb1b31286db849cb14cbc507ba036217d47744b",
  "cid": "QmV18c7c2ad91a567c16e3aab21d5cb1b31286db849c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292835,
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
      "evaluated_at": 1760292835
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
  "sig": "afee688e266f2786b0cae31f76d48c9ae2eaec204dd98f545a1d72758c40b23f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000023914154
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 206, 'threshold': 50, 'total_amount': 98535568, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 205, 'first_seen': 1760285764, 'matching_hash': '45ff85674ff7fdbe'}}}