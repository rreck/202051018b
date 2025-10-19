```json
{
  "id": "c1cbc1554066a668",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289070,
  "host_pid": "9e6742732c60:1",
  "hash": "6e03e2e22f8743cc8f17d4dc3de392347ff6dd51cf934b42e179c1d6f3b1274d",
  "cid": "QmV16e03e2e22f8743cc8f17d4dc3de392347ff6dd51",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289070,
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
      "evaluated_at": 1760289070
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
  "sig": "6c673639017d00f1e00b2b928c551e505125ec5c219f0042bd1db794af824bd2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 112, 'threshold': 50, 'total_amount': 35643776, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 111, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}