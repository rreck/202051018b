```json
{
  "id": "876fb03286cb17d4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290872,
  "host_pid": "9e6742732c60:1",
  "hash": "6e78580d44feca59b24fa0f3ab3a94abefe02b506b82623657388bf608f59237",
  "cid": "QmV16e78580d44feca59b24fa0f3ab3a94abefe02b50",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290872,
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
      "evaluated_at": 1760290872
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
  "sig": "44d5ed6057379052354ff60f8a372ac0f9477f3f13f56f8ad27bd30c31b1bf39"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271105789
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 161, 'threshold': 50, 'total_amount': 43647422, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 160, 'first_seen': 1760285764, 'matching_hash': 'b50c8d05dbdb14ee'}}}