```json
{
  "id": "bec6e300f4a3cd71",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285943,
  "host_pid": "9e6742732c60:1",
  "hash": "c0a4fe766941b916b0a817b64ae082a77dadc249c570ea840070869329d24563",
  "cid": "QmV1c0a4fe766941b916b0a817b64ae082a77dadc249",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285943,
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
      "evaluated_at": 1760285943
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
  "sig": "8f76e2d72d7dd5532448ecf15e777c248655b14390d26e672bc0a58f07af17ae"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201464866805
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 8, 'first_seen': 1760285764, 'matching_hash': '8f846e2074b125b7'}}}