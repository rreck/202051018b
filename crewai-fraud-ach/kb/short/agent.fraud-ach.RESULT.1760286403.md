```json
{
  "id": "d75ae7dab7d55dd0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286403,
  "host_pid": "9e6742732c60:1",
  "hash": "ae93ed73f933063b1a2d49480500d6b7b7880fd802f007c23809c9a8765d4c71",
  "cid": "QmV1ae93ed73f933063b1a2d49480500d6b7b7880fd8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286403,
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
      "evaluated_at": 1760286403
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
  "sig": "ab3d852285c117f7f5277d46bd8dabedf615622191d22dcb5a8ff9e3f1305c1d"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105153385568
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 23, 'first_seen': 1760285763, 'matching_hash': '556aff2bced704f0'}}}