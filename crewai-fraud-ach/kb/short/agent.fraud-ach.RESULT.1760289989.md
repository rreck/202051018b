```json
{
  "id": "2cfabd2535e4fd48",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289989,
  "host_pid": "9e6742732c60:1",
  "hash": "e318de47a21f2d385778f974d14f9e994c74720fab04b831efb1767329b513c8",
  "cid": "QmV1e318de47a21f2d385778f974d14f9e994c74720f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289989,
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
      "evaluated_at": 1760289989
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
  "sig": "9c21cb10dfbfcce93e5153d7fb578ece9af4048965a614e1de0d32bad1935c25"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022135017
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 138, 'threshold': 50, 'total_amount': 10290246, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 137, 'first_seen': 1760285765, 'matching_hash': 'ca41710ea386559e'}}}