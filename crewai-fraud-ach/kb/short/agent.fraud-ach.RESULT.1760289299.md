```json
{
  "id": "6a5010790ffd4f0a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289299,
  "host_pid": "9e6742732c60:1",
  "hash": "e89f4bb2a1de6cb5cc82f6eb14071826c832f645894998fcdfe71614b2c54cfa",
  "cid": "QmV1e89f4bb2a1de6cb5cc82f6eb14071826c832f645",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289299,
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
      "evaluated_at": 1760289299
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
  "sig": "93837fcf982a3020b73913ae939460b7f9132d2e31e33e05fa6b20f209e545a2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025895266
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 119, 'threshold': 50, 'total_amount': 33784100, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 118, 'first_seen': 1760285763, 'matching_hash': '9ac81502eabc8fa5'}}}