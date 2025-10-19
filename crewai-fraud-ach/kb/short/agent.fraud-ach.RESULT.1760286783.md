```json
{
  "id": "e907405f03ef8365",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286783,
  "host_pid": "9e6742732c60:1",
  "hash": "79e1c6bf691800df3c36f6cb576c98b7bab7a882e23b2652fffc98c5c2e21ef0",
  "cid": "QmV179e1c6bf691800df3c36f6cb576c98b7bab7a882",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286783,
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
      "evaluated_at": 1760286783
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
  "sig": "70b589aa7e0f648ec6266ebc45201c9a3d7ce8f17d95c5d4f7dd13b2d83f21c8"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 026009595764750
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 36, 'first_seen': 1760285763, 'matching_hash': '81dd493231a1d242'}}}