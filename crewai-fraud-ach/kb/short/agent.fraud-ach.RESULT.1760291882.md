```json
{
  "id": "1f7a5c8e46e12a34",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291882,
  "host_pid": "9e6742732c60:1",
  "hash": "cfb7c1be9a922988b1a7ce14747c2bc82e479b05c4b2ce23127098b3fd8a8def",
  "cid": "QmV1cfb7c1be9a922988b1a7ce14747c2bc82e479b05",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291882,
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
      "evaluated_at": 1760291882
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
  "sig": "dd937a7c4a4f74d123a1bccbc82df14945e22840e3a15e138da4040511780fab"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469533124
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 185, 'threshold': 50, 'total_amount': 37152440, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 184, 'first_seen': 1760285765, 'matching_hash': '99a5c6f080ea1552'}}}