```json
{
  "id": "d2d192f34b0e2879",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293764,
  "host_pid": "9e6742732c60:1",
  "hash": "97b7b2262d37e8ab61e4bf408d40f0fbcc84cfdf8be1b48d3943544fe9c50f53",
  "cid": "QmV197b7b2262d37e8ab61e4bf408d40f0fbcc84cfdf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293764,
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
      "evaluated_at": 1760293764
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
  "sig": "2a41b8f16f70df285e38d8bfc0b83b74354ae618dec466b9085634e5cc285e4d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274521172
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 225, 'threshold': 50, 'total_amount': 23985450, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 224, 'first_seen': 1760285764, 'matching_hash': 'cfb56b896e519b42'}}}