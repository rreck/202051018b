```json
{
  "id": "b1de8ce96a321b06",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286193,
  "host_pid": "9e6742732c60:1",
  "hash": "fdde82b83c8a072c954fccd144622e3d32f0ca30a2efb2f47776563509b18faf",
  "cid": "QmV1fdde82b83c8a072c954fccd144622e3d32f0ca30",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286193,
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
      "evaluated_at": 1760286193
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
  "sig": "03e390bb8f0321239138d7ec2e2df92926437d41f2d2289f072869103a0fcbb4"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 026009590866940
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 16, 'first_seen': 1760285765, 'matching_hash': '66ff896a34603a53'}}}