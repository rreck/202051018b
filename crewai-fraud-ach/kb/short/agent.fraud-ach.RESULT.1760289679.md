```json
{
  "id": "e4df80b1886fa5ba",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289679,
  "host_pid": "9e6742732c60:1",
  "hash": "8b3bae413ddd55cd6895deaccad08f0d5903002cf896ac408d24845c8e3cd8d4",
  "cid": "QmV18b3bae413ddd55cd6895deaccad08f0d5903002c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289679,
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
      "evaluated_at": 1760289679
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
  "sig": "518b109e9c96bc9d567c10a92dcc1e42fc41f29be54e04824e758ba44a49dbd0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274968720
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 130, 'threshold': 50, 'total_amount': 48507420, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 129, 'first_seen': 1760285763, 'matching_hash': '69fe72c937d65071'}}}