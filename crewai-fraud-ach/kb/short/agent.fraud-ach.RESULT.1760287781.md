```json
{
  "id": "fd28760ca89335fd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287781,
  "host_pid": "9e6742732c60:1",
  "hash": "8ca176b57efd743107f1f1d0911acd768faf9f91910a366c30d71ce85a2fbd6f",
  "cid": "QmV18ca176b57efd743107f1f1d0911acd768faf9f91",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287781,
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
      "evaluated_at": 1760287781
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
  "sig": "cf945c87a6353e2ac986ced5a2e194455ea30ef4b81396bef1d5e1a49394a0a1"
}
```

Fraud detected: duplicate_transaction (score: 89)
Transaction: 044000033554857
Details: {'velocity': {'fraud_detected': True, 'risk_score': 94, 'details': {'transaction_count': 72, 'threshold': 50, 'total_amount': 34369704, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 71, 'first_seen': 1760285763, 'matching_hash': '1f36f93e880b57ba'}}}