```json
{
  "id": "954038bde5f89bde",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288276,
  "host_pid": "9e6742732c60:1",
  "hash": "e915ab8943fcecd39ba0561522e63ae763a5727043d726e57101d42b94ff27f3",
  "cid": "QmV1e915ab8943fcecd39ba0561522e63ae763a57270",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288276,
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
      "evaluated_at": 1760288276
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
  "sig": "917d04f216c80c9b476c925e289e921ff9393458081860324a3e59c85aeb7041"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201468284841
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 88, 'threshold': 50, 'total_amount': 16482664, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 87, 'first_seen': 1760285764, 'matching_hash': 'af26bab6e9f38d2a'}}}