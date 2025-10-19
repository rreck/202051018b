```json
{
  "id": "d042be2b3141b826",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293856,
  "host_pid": "9e6742732c60:1",
  "hash": "d84e65bb300fad56e92abe7ff9a9726f72562d27d7eed020b23a913196efc5eb",
  "cid": "QmV1d84e65bb300fad56e92abe7ff9a9726f72562d27",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293856,
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
      "evaluated_at": 1760293856
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
  "sig": "6b630c29deba5c3ecca55b7039a8e449d28baa8cdc4a760c2ada2c401c2aefa4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025654087
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 227, 'threshold': 50, 'total_amount': 31733465, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 226, 'first_seen': 1760285763, 'matching_hash': '431eabbdd05dc2b1'}}}