```json
{
  "id": "154dece87d7a50ca",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289689,
  "host_pid": "9e6742732c60:1",
  "hash": "679ab5a6c62e357725cd09684256078ea59753a199388b09c6fb22e951b6cbd2",
  "cid": "QmV1679ab5a6c62e357725cd09684256078ea59753a1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289689,
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
      "evaluated_at": 1760289689
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
  "sig": "352c5d53e8324e2e742ddbae2cb8f6290eb7953b8ec6c8072b578065796cedc7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000031029200
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 130, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 129, 'first_seen': 1760285763, 'matching_hash': '80e7fe619ff961e0'}}}