```json
{
  "id": "44456bb40d713a65",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287605,
  "host_pid": "9e6742732c60:1",
  "hash": "07a1adfa50a25148c30ee0efeadb5b9f65b4f7e5c4f8e2dcf153046e39a5c3fb",
  "cid": "QmV107a1adfa50a25148c30ee0efeadb5b9f65b4f7e5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287605,
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
      "evaluated_at": 1760287605
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
  "sig": "f21ff6c30bfa26931fcb6811fc74f88a3eef3fe05696ce24f2c7e884a1ca0f18"
}
```

Fraud detected: duplicate_transaction (score: 83)
Transaction: 121000243604729
Details: {'velocity': {'fraud_detected': True, 'risk_score': 82, 'details': {'transaction_count': 66, 'threshold': 50, 'total_amount': 32783784, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 65, 'first_seen': 1760285763, 'matching_hash': '930ed718dd68e21a'}}}