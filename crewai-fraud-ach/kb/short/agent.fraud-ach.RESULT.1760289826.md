```json
{
  "id": "bececbe860f1e683",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289826,
  "host_pid": "9e6742732c60:1",
  "hash": "5a6ee37c0c73d226d97b8a010abbb53cb5a8f9a2b2e16bab6249a52455fd892f",
  "cid": "QmV15a6ee37c0c73d226d97b8a010abbb53cb5a8f9a2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289826,
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
      "evaluated_at": 1760289826
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
  "sig": "6e93b6f2e6d7ff3b2e7672cdc52c525d88993935ac6e520d9471bc82c9e1c8d4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154730054
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 134, 'threshold': 50, 'total_amount': 36080840, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 133, 'first_seen': 1760285763, 'matching_hash': '3072a79f51416ab8'}}}