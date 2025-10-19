```json
{
  "id": "793416f97506000f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287642,
  "host_pid": "9e6742732c60:1",
  "hash": "bfa264ed14ef2c2edf0f46421fd6c19f9d7d3362a8ff08edb08853d352acd47c",
  "cid": "QmV1bfa264ed14ef2c2edf0f46421fd6c19f9d7d3362",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287642,
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
      "evaluated_at": 1760287642
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
  "sig": "b1c70877b4fb9636bc72fab4e4aec4af43ec4869aa5ff56b9b4eb161053a9a2f"
}
```

Fraud detected: duplicate_transaction (score: 84)
Transaction: 111000026725963
Details: {'velocity': {'fraud_detected': True, 'risk_score': 84, 'details': {'transaction_count': 67, 'threshold': 50, 'total_amount': 13524486, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 66, 'first_seen': 1760285765, 'matching_hash': '729970816697b41b'}}}