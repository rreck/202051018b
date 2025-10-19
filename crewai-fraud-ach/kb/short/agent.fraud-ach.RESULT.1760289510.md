```json
{
  "id": "9a2c222f55f6b201",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289510,
  "host_pid": "9e6742732c60:1",
  "hash": "249a283588df681ddfde4a2991e4ee8a5b823efa90d37b898dd94ad8b706aa89",
  "cid": "QmV1249a283588df681ddfde4a2991e4ee8a5b823efa",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289510,
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
      "evaluated_at": 1760289510
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
  "sig": "54ef3567d3206f198d5a1ef09ad5c9462e6fe8bebe32e48955d85d04d1a3b803"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201467134805
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 125, 'threshold': 50, 'total_amount': 34005625, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 124, 'first_seen': 1760285763, 'matching_hash': 'bc3c56d4b0e7489d'}}}