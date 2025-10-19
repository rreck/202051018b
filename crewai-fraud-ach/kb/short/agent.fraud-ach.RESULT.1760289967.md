```json
{
  "id": "44339e4894866b15",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289967,
  "host_pid": "9e6742732c60:1",
  "hash": "65e4a3723d8d0478389d032afe15f488e979800ef2e060465d7640eade659fa3",
  "cid": "QmV165e4a3723d8d0478389d032afe15f488e979800e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289967,
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
      "evaluated_at": 1760289967
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
  "sig": "e53c7c9546b13028f52662061daa14a28f3cbbdd965897f0699a9e8799ddc2ae"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000029536226
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 138, 'threshold': 50, 'total_amount': 10048608, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 137, 'first_seen': 1760285763, 'matching_hash': 'ee8686fc8d545b2d'}}}