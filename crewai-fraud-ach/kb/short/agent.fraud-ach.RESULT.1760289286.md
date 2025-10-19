```json
{
  "id": "bb93ef945bcab47e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289286,
  "host_pid": "9e6742732c60:1",
  "hash": "118bc5eb8f3eb412dabbff102c4f72a5b53deb0f0bd4cd67579e362eeba229fd",
  "cid": "QmV1118bc5eb8f3eb412dabbff102c4f72a5b53deb0f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289286,
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
      "evaluated_at": 1760289286
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
  "sig": "5e869ec1b2a119c7bd0017f1c7bcfd4f63dc64a38dda834bf82f2852b3fbe0cf"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000023724402
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 119, 'threshold': 50, 'total_amount': 28121009, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 118, 'first_seen': 1760285763, 'matching_hash': '3d4ab0f371876a2a'}}}