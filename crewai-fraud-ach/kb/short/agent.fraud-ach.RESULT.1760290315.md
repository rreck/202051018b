```json
{
  "id": "b99edb10e87c8090",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290315,
  "host_pid": "9e6742732c60:1",
  "hash": "cb6617fcc0119feebb5961d0369b84ddd02ea2732f00bd3cab3579942fc2bab4",
  "cid": "QmV1cb6617fcc0119feebb5961d0369b84ddd02ea273",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290315,
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
      "evaluated_at": 1760290315
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
  "sig": "05fcd7990958345935e3a3c8ddd4369c8bd751901179578667ded6635ed7579b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029230021
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 147, 'threshold': 50, 'total_amount': 48140001, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 146, 'first_seen': 1760285763, 'matching_hash': 'f06e706b59004f2f'}}}d_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}