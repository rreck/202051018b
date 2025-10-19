```json
{
  "id": "9bd9e9395a013145",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288954,
  "host_pid": "9e6742732c60:1",
  "hash": "99a8b412cc871dfa6fe3afef88989d803ca4366043932625d69d70e31d8caf17",
  "cid": "QmV199a8b412cc871dfa6fe3afef88989d803ca43660",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288954,
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
      "evaluated_at": 1760288954
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
  "sig": "4dfaeb8b94d140c3daf1f8196538df33dc6e97749f6a20232504bad4fd987101"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201468629827
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 109, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 108, 'first_seen': 1760285763, 'matching_hash': 'f998250ed7d87b2f'}}}