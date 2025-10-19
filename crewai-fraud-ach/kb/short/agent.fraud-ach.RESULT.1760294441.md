```json
{
  "id": "db277f936f7615a3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294441,
  "host_pid": "9e6742732c60:1",
  "hash": "4c05faee1fbd736b21b71ec343931115a7a28734b8f6494f1b677fa9061cd20d",
  "cid": "QmV14c05faee1fbd736b21b71ec343931115a7a28734",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294441,
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
      "evaluated_at": 1760294441
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
  "sig": "f59bf80e12cf49b342063def5995338c5cbeb2552157e3000293b6e3592c7d45"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100276179264
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 238, 'threshold': 50, 'total_amount': 40806528, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 237, 'first_seen': 1760285763, 'matching_hash': 'cb2614db0e970d70'}}}}