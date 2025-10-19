```json
{
  "id": "97f652b5731550f7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285807,
  "host_pid": "9e6742732c60:1",
  "hash": "471ae494b85c6252c45bb4a8caa4a58005e6d4683724fa7d7f87b959b2cc3bfa",
  "cid": "QmV1471ae494b85c6252c45bb4a8caa4a58005e6d468",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285807,
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
      "evaluated_at": 1760285807
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
  "sig": "a697027163ffc1fc5621e8db00457165f45f0f2a6d31c0a543d655568bdbe98b"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 026009593563572
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 2, 'first_seen': 1760285765, 'matching_hash': 'b3bf50e818486c57'}}}