```json
{
  "id": "6db383be6ca637e1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286553,
  "host_pid": "9e6742732c60:1",
  "hash": "c8988d52c1312c0dea4ed1b87e781942bc3dfbfaaca77840a048fba70a3a018d",
  "cid": "QmV1c8988d52c1312c0dea4ed1b87e781942bc3dfbfa",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286553,
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
      "evaluated_at": 1760286553
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
  "sig": "7c46be029daf4f5aac6f36e4e06307f957ad454b30e05e0a4474f0a5138d56e7"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 063100278037585
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 28, 'first_seen': 1760285763, 'matching_hash': '27cb7a10328c75d5'}}}ue, 'risk_score': 85, 'details': {'duplicate_count': 28, 'first_seen': 1760285764, 'matching_hash': 'fe2a7bcd9137a402'}}}