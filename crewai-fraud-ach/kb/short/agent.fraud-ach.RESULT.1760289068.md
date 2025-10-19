```json
{
  "id": "1313efad227d7f5e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289068,
  "host_pid": "9e6742732c60:1",
  "hash": "b19dac7492688812e6bddc47de3a818bbaa03eaacfc34fc7f2982bcd1beb05ca",
  "cid": "QmV1b19dac7492688812e6bddc47de3a818bbaa03eaa",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289068,
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
      "evaluated_at": 1760289068
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
  "sig": "50dd76f7131710a62938b2b7d52b69ada2882b822acd8137b0fc1092dd9ce1bc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201463448865
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 112, 'threshold': 50, 'total_amount': 19247536, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 111, 'first_seen': 1760285765, 'matching_hash': '5a565595f8571aef'}}}