```json
{
  "id": "ba801ae9ab09cb8d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294673,
  "host_pid": "9e6742732c60:1",
  "hash": "c671e7a0425b15a3c40630fa39dd288533e5f0a411809b780e413495eea12178",
  "cid": "QmV1c671e7a0425b15a3c40630fa39dd288533e5f0a4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294673,
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
      "evaluated_at": 1760294673
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
  "sig": "6b8011e9ef94227685fd52d5236665e17f163289e11b4426250b7fe1c53fc1bb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596468860
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 242, 'threshold': 50, 'total_amount': 18302460, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 241, 'first_seen': 1760285763, 'matching_hash': 'e06c0748f018586e'}}}