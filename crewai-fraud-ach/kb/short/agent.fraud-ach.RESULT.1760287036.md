```json
{
  "id": "7302e4ac50382f0e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287036,
  "host_pid": "9e6742732c60:1",
  "hash": "07e92be3312d10f2770d37fe61e99637a325b8636681e840096af0da31156457",
  "cid": "QmV107e92be3312d10f2770d37fe61e99637a325b863",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287036,
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
      "evaluated_at": 1760287037
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
  "sig": "d73a3aac2015293a5ec08531b7133899951da0fcd0c1263082a712bd5f98c69b"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000023218255
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 45, 'first_seen': 1760285763, 'matching_hash': '1151ecc015fd8f1a'}}}ue, 'risk_score': 85, 'details': {'duplicate_count': 45, 'first_seen': 1760285763, 'matching_hash': '3d4ab0f371876a2a'}}}