```json
{
  "id": "ccce09b96e084d6d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286794,
  "host_pid": "9e6742732c60:1",
  "hash": "c23837c895cc5183b6a597060c5aa46a839ac262822d665adf2fa75d106199f9",
  "cid": "QmV1c23837c895cc5183b6a597060c5aa46a839ac262",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286794,
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
      "evaluated_at": 1760286794
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
  "sig": "8ef261392784e5589d6d7c19e156942f83bb63071e241db3de76e5d974027eb1"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 026009597862857
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 36, 'first_seen': 1760285765, 'matching_hash': 'eac3ff1003c03af8'}}}