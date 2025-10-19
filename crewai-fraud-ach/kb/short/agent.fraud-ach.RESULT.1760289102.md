```json
{
  "id": "226d23dfbc8b990d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289102,
  "host_pid": "9e6742732c60:1",
  "hash": "d17df653a5b3b41db6d0623a279e9f3346e9446093313c3e980bab3f9119ed75",
  "cid": "QmV1d17df653a5b3b41db6d0623a279e9f3346e94460",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289102,
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
      "evaluated_at": 1760289102
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
  "sig": "5a961f4287c9ab84388e61dc7c61b78f13416a575b68ea560450543ee7356e8e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469007601
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 113, 'threshold': 50, 'total_amount': 11438086, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 112, 'first_seen': 1760285765, 'matching_hash': '9208fda71b3c290c'}}}