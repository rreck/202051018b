```json
{
  "id": "a225147db0711964",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290354,
  "host_pid": "9e6742732c60:1",
  "hash": "6f9826869c9e2c2867a97fb4fac063f00fd26abfb7d4028682bb9a5b5897eeb5",
  "cid": "QmV16f9826869c9e2c2867a97fb4fac063f00fd26abf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290354,
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
      "evaluated_at": 1760290354
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
  "sig": "b4506a3218b284ea4acc1bbb9972aa12815e0c8589d6764b35ac987fa3c67e58"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100270739022
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 148, 'threshold': 50, 'total_amount': 42710580, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 147, 'first_seen': 1760285763, 'matching_hash': '068659374d77a711'}}}