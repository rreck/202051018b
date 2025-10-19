```json
{
  "id": "3bb21c2f3d41bea6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287270,
  "host_pid": "9e6742732c60:1",
  "hash": "7c94be808970d5c9b84bf1f254c61027ba586f19167d983606c368a808c41c2e",
  "cid": "QmV17c94be808970d5c9b84bf1f254c61027ba586f19",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287270,
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
      "evaluated_at": 1760287270
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "9455c3224bbadede033b0a843dcaf58501b12329a43bbe0aa9bb6e7d25aeda19"
}
```

Fraud detected: duplicate_transaction (score: 71)
Transaction: 031201466679999
Details: {'velocity': {'fraud_detected': True, 'risk_score': 58, 'details': {'transaction_count': 54, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 53, 'first_seen': 1760285763, 'matching_hash': '7890640eadac4bcb'}}}