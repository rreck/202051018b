```json
{
  "id": "ffd73a23f8d74893",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289301,
  "host_pid": "9e6742732c60:1",
  "hash": "09426f469af04b8852c27686ee2b2c4f117c93b97e3cd301ecc17b7c8567278c",
  "cid": "QmV109426f469af04b8852c27686ee2b2c4f117c93b9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289301,
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
      "evaluated_at": 1760289301
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
  "sig": "3f8e7958c9b8384e14cb7a7372910adbf33748fb681a0f63cf9d2589f672829e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271105789
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 119, 'threshold': 50, 'total_amount': 32261138, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 118, 'first_seen': 1760285764, 'matching_hash': 'b50c8d05dbdb14ee'}}}