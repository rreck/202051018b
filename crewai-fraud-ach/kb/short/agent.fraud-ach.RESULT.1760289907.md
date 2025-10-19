```json
{
  "id": "96315560990fd9d9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289907,
  "host_pid": "9e6742732c60:1",
  "hash": "7ccbfdea10c7e0507bd1c07dfeb28545b03b5cb9542ec396a4c4230a3a9cf887",
  "cid": "QmV17ccbfdea10c7e0507bd1c07dfeb28545b03b5cb9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289907,
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
      "evaluated_at": 1760289907
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
  "sig": "a8966eacc0e5c905e486738c6e5afe07081e662fe537b70e944f74b5e9c581e2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201467134805
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 136, 'threshold': 50, 'total_amount': 36998120, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 135, 'first_seen': 1760285763, 'matching_hash': 'bc3c56d4b0e7489d'}}}