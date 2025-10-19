```json
{
  "id": "030402c47effb437",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287715,
  "host_pid": "9e6742732c60:1",
  "hash": "895dfd7a44e5d2b12aa24dc63891e7e3315905791642b80a93f992035e85f7f0",
  "cid": "QmV1895dfd7a44e5d2b12aa24dc63891e7e331590579",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287715,
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
      "evaluated_at": 1760287715
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
  "sig": "eced85553d6132b1bb6ccee6e46aa0bdaa1d064f766a51f8c1fbab99bbbde4c2"
}
```

Fraud detected: duplicate_transaction (score: 87)
Transaction: 121000248845664
Details: {'velocity': {'fraud_detected': True, 'risk_score': 90, 'details': {'transaction_count': 70, 'threshold': 50, 'total_amount': 16423190, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 69, 'first_seen': 1760285763, 'matching_hash': 'd68dab2741390ae3'}}}d_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}