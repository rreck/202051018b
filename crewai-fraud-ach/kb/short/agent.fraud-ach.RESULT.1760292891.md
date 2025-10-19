```json
{
  "id": "8f6b7427f37f5284",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292891,
  "host_pid": "9e6742732c60:1",
  "hash": "d3b12af1d543a11c115b42541e1859876e01ccdcc0c24376dbe281ea790dc85b",
  "cid": "QmV1d3b12af1d543a11c115b42541e1859876e01ccdc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292891,
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
      "evaluated_at": 1760292891
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
  "sig": "a210addf3aecc72be4df1ccf9b098882c3249a2d71f2dddca9f2bb0957f08ea0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464887509
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 207, 'threshold': 50, 'total_amount': 99752679, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 206, 'first_seen': 1760285763, 'matching_hash': '8c09836a51c1ceac'}}}