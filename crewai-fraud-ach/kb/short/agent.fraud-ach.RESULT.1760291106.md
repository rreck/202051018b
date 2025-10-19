```json
{
  "id": "1ad54bcdcb461378",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291106,
  "host_pid": "9e6742732c60:1",
  "hash": "ecf84d50b4208a0b3a8a8ad89ee60bb8786160904e016c4f994ee7c0ff6891b0",
  "cid": "QmV1ecf84d50b4208a0b3a8a8ad89ee60bb878616090",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291106,
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
      "evaluated_at": 1760291106
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
  "sig": "8dd72a44f73d6400742ce5ae28017196b960f8ea1db1fa5659c1956493c5b039"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000032306947
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 167, 'threshold': 50, 'total_amount': 12876535, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 166, 'first_seen': 1760285763, 'matching_hash': '0095d1181b74b3e8'}}}