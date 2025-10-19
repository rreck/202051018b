```json
{
  "id": "ba94a12c388324ca",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287024,
  "host_pid": "9e6742732c60:1",
  "hash": "1022f7784b5dddfb59e1cd3081ffd687aeb77f2d938c8e91f79aa0f53c40a68c",
  "cid": "QmV11022f7784b5dddfb59e1cd3081ffd687aeb77f2d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287024,
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
      "evaluated_at": 1760287024
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
  "sig": "b0e27a4e78f018bee70a3de1b294fc39d576d126f62f751a0fdedce4bf256ab8"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 063100275925775
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 44, 'first_seen': 1760285765, 'matching_hash': 'faef3b4bfd0d33cd'}}}