```json
{
  "id": "d3ed89d15c9360fa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286761,
  "host_pid": "9e6742732c60:1",
  "hash": "59e63f6c7f13099f9dc2e59ee9145de5190e9159ab431fe55cb07394b724afce",
  "cid": "QmV159e63f6c7f13099f9dc2e59ee9145de5190e9159",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286761,
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
      "evaluated_at": 1760286761
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
  "sig": "482e8d39668e1a762eb05a175fc3fab112d6be6c7a7dba15e50d3c5be8532f45"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000241561723
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 35, 'first_seen': 1760285764, 'matching_hash': '61d0611cbf39c4a3'}}}