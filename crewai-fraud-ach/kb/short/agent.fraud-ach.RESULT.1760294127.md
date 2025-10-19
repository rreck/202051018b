```json
{
  "id": "e03c4610de229c4a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294127,
  "host_pid": "9e6742732c60:1",
  "hash": "85c464a83522dd3bb2a7040e0f133d341892d4a7947443f64be2a174bea817da",
  "cid": "QmV185c464a83522dd3bb2a7040e0f133d341892d4a7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294127,
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
      "evaluated_at": 1760294128
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
  "sig": "d47b20ed5365bea451e9e1ccaf2bd20c3bb3a6fb1b637fbce8954b73e62ea032"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271137444
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 232, 'threshold': 50, 'total_amount': 52572592, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 231, 'first_seen': 1760285763, 'matching_hash': 'cc450f1d426424de'}}}