```json
{
  "id": "c057ecb717b410b1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286757,
  "host_pid": "9e6742732c60:1",
  "hash": "caf58777c1b233ae38580ae85c493b3a6365fdec29f1b7199ef9bbc4d7568b78",
  "cid": "QmV1caf58777c1b233ae38580ae85c493b3a6365fdec",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286757,
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
      "evaluated_at": 1760286757
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
  "sig": "7d6015ec9e65358bf95a394c1148de4ece4f696c6d82cd9adde42d8273efd585"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465682795
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 112, 'threshold': 50, 'total_amount': 28214480, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 111, 'first_seen': 1760284979, 'matching_hash': 'c9bd5d9b74477b1c'}}}