```json
{
  "id": "5b631f4acd327d0b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293480,
  "host_pid": "9e6742732c60:1",
  "hash": "73066a00dd352d7c05b481f3703506c4b433b4aadf92e18150af4034b048ddd9",
  "cid": "QmV173066a00dd352d7c05b481f3703506c4b433b4aa",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293480,
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
      "evaluated_at": 1760293480
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
  "sig": "6c205593e228cd6c3f77929144550767d31afb97c0cb5f7afd97f84df710c8ea"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596468860
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 219, 'threshold': 50, 'total_amount': 16562970, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 218, 'first_seen': 1760285763, 'matching_hash': 'e06c0748f018586e'}}}