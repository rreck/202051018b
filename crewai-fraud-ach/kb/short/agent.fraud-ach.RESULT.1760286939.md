```json
{
  "id": "d756070ff12885fd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286939,
  "host_pid": "9e6742732c60:1",
  "hash": "0103ee109c816baf10a73c885ac71f1eaa17f8742634f9d3e3d330f062abcf3f",
  "cid": "QmV10103ee109c816baf10a73c885ac71f1eaa17f874",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286939,
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
      "evaluated_at": 1760286939
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
  "sig": "f83be67e51f972aaf1d2fd59ee11ae48a64dacddc01c884e826d9b87c892455a"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000022135017
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 41, 'first_seen': 1760285765, 'matching_hash': 'ca41710ea386559e'}}}