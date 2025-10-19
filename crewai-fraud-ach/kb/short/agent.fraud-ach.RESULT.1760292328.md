```json
{
  "id": "253b204071d24277",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292328,
  "host_pid": "9e6742732c60:1",
  "hash": "99081fd5e69744afd493b287960197606449ff2e130a3f04ac5d8911a7d9fa4f",
  "cid": "QmV199081fd5e69744afd493b287960197606449ff2e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292328,
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
      "evaluated_at": 1760292328
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
  "sig": "7ec297a206a4cd0215e234b510d43f8a408b991bea7e100fdb4ed797f38885be"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100276997857
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 195, 'threshold': 50, 'total_amount': 92770665, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 194, 'first_seen': 1760285763, 'matching_hash': 'b73e9a6de72cc131'}}}