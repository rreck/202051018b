```json
{
  "id": "6dd2680c85386394",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294921,
  "host_pid": "9e6742732c60:1",
  "hash": "fadbb23773eaf2c9ffa9d960a4aeedce8dd4a70670f522119a44eadc2e4fec2a",
  "cid": "QmV1fadbb23773eaf2c9ffa9d960a4aeedce8dd4a706",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294921,
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
      "evaluated_at": 1760294921
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
  "sig": "5174d574a250c100e9b9c214ad59782877063799d4226edf3e4928f0b570e91c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591167362
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 247, 'threshold': 50, 'total_amount': 77081784, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 246, 'first_seen': 1760285763, 'matching_hash': '24df3db171a5add1'}}} {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '868351851', 'validation_error': 'Invalid routing number checksum'}}}