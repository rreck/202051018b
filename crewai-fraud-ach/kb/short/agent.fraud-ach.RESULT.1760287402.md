```json
{
  "id": "8fa92a430da4a1fa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287402,
  "host_pid": "9e6742732c60:1",
  "hash": "8f9243af1e64511f7dd2e7853e811fd177cf7f7b99097856f04d690747a89339",
  "cid": "QmV18f9243af1e64511f7dd2e7853e811fd177cf7f7b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287402,
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
      "evaluated_at": 1760287402
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "fb22aefc455eced8a53a0d6f7ed158e309ab1295373eb05f7b18685dd659afb9"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000026299785
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 59, 'threshold': 50, 'total_amount': 25937049, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 58, 'first_seen': 1760285763, 'matching_hash': 'dc2585930aebf220'}}}