```json
{
  "id": "d3b89c1eacd1488b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289626,
  "host_pid": "9e6742732c60:1",
  "hash": "0d31323afc44e33d49cc0c38205905dd7cfd8200641ede9a9d2b69e2a5c1a937",
  "cid": "QmV10d31323afc44e33d49cc0c38205905dd7cfd8200",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289626,
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
      "evaluated_at": 1760289626
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
  "sig": "0318312c288e294da73909893eb098e08dbc5615c6bea057e9747f5847bd4afa"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 128, 'threshold': 50, 'total_amount': 40735744, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 127, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}