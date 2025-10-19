```json
{
  "id": "a8234a9ff668270a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286937,
  "host_pid": "9e6742732c60:1",
  "hash": "3e497afb91222ff247c63e9758dec18ebb087eb2dcfb8145709eefc5127009ce",
  "cid": "QmV13e497afb91222ff247c63e9758dec18ebb087eb2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286937,
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
      "evaluated_at": 1760286937
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "4ef67d2078050ec65f32604de7deb5ed3f341d0c2fd6e6426177c4f51a921504"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 026009599905929
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 16315740, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 41, 'first_seen': 1760285765, 'matching_hash': 'da08c58383816f07'}}}