```json
{
  "id": "d327f6a3c95a1aa0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293962,
  "host_pid": "9e6742732c60:1",
  "hash": "29db7a4cc1eb17e976ada40fc4a9a2fd364366b2f9fc47c7e50c8037d37350ea",
  "cid": "QmV129db7a4cc1eb17e976ada40fc4a9a2fd364366b2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293962,
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
      "evaluated_at": 1760293962
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
  "sig": "a04c6d82d974cc50fc852ff6e03a5462ef2207c1e3007f2e8d395517eaba109f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000246132965
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 229, 'threshold': 50, 'total_amount': 100689239, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 228, 'first_seen': 1760285763, 'matching_hash': 'ed6ec2b6e100ea2c'}}}