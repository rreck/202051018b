```json
{
  "id": "b0675c6f58195906",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289013,
  "host_pid": "9e6742732c60:1",
  "hash": "e9e636547e1783e42f80066a8146cf0697b5059da7e5189a8058a8e30fc3e249",
  "cid": "QmV1e9e636547e1783e42f80066a8146cf0697b5059d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289013,
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
      "evaluated_at": 1760289013
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "invalid_routing",
    "risk_critical"
  ],
  "sig": "dfef00664568e25e367c188bd584463619204e8203c6afa21ddb406f366680af"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 561028999821965
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 111, 'threshold': 50, 'total_amount': 15538779, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 110, 'first_seen': 1760285763, 'matching_hash': '09f745cfd1242827'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '561028991', 'validation_error': 'Invalid routing number checksum'}}}