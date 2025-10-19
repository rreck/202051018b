```json
{
  "id": "bd3d7ee6ad2648f4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288534,
  "host_pid": "9e6742732c60:1",
  "hash": "b096e424bed9fc4060e16fadaae23c9e17083a4eb5579ba5e135f43329384762",
  "cid": "QmV1b096e424bed9fc4060e16fadaae23c9e17083a4e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288534,
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
      "evaluated_at": 1760288534
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
  "sig": "b16616b9fde15b4ffac0a87ba1175664c342685ce9c5bd7d70ddb251c27b2bce"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271105789
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 96, 'threshold': 50, 'total_amount': 26025792, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 95, 'first_seen': 1760285764, 'matching_hash': 'b50c8d05dbdb14ee'}}}