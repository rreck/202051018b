```json
{
  "id": "eea47447f308b0f8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292872,
  "host_pid": "9e6742732c60:1",
  "hash": "d3c57029cb4d0c89b0ad92e1c959bbf876091aeffa52dc821016a266b2c10e69",
  "cid": "QmV1d3c57029cb4d0c89b0ad92e1c959bbf876091aef",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292872,
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
      "evaluated_at": 1760292872
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
  "sig": "dac4a14e857bb568a198bccba16f1e87cfdc9b57d95650eb3448411304c38fb8"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 261425243879882
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 207, 'threshold': 50, 'total_amount': 68381829, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 206, 'first_seen': 1760285763, 'matching_hash': 'bea146cfc71ce9bb'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '261425248', 'validation_error': 'Invalid routing number checksum'}}}