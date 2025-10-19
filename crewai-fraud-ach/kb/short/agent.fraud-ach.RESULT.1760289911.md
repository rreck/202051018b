```json
{
  "id": "3159613ceaef437d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289911,
  "host_pid": "9e6742732c60:1",
  "hash": "0b9798b1d6c4a3d53522fab4ef0fbc51740ffb287c48af9d60e779ba85b77a08",
  "cid": "QmV10b9798b1d6c4a3d53522fab4ef0fbc51740ffb28",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289911,
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
      "evaluated_at": 1760289911
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
  "sig": "8d21378936f4cf14d1c54d8db4704e44d7e594638d5c0622149d55630f4fb8df"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 011137004104696
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 136, 'threshold': 50, 'total_amount': 16597304, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 135, 'first_seen': 1760285765, 'matching_hash': 'b4a76c6b789f42f2'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '011137004', 'validation_error': 'Invalid routing number checksum'}}}