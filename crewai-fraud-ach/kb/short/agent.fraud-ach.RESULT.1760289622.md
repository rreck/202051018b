```json
{
  "id": "8ef06802dcb8210e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289622,
  "host_pid": "9e6742732c60:1",
  "hash": "af887a7d87c433de3976b4d0df0a745518e7d590d4a8d1d6c3e8324a8e384041",
  "cid": "QmV1af887a7d87c433de3976b4d0df0a745518e7d590",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289622,
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
      "evaluated_at": 1760289622
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
  "sig": "0be1fded6cd12fdd9f14045f14c5a636e5bf4ef69931f170e7367e98057cc8bf"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274578801
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 128, 'threshold': 50, 'total_amount': 22481920, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 127, 'first_seen': 1760285765, 'matching_hash': 'c58645b7bcecdbfd'}}}