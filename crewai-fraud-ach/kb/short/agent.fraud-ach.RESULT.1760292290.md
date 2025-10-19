```json
{
  "id": "694b69d1b4c04590",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292290,
  "host_pid": "9e6742732c60:1",
  "hash": "313d50e84a013ba0177990f56ab7181299e08d1c3764ed29b97ea5e1d67da77b",
  "cid": "QmV1313d50e84a013ba0177990f56ab7181299e08d1c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292290,
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
      "evaluated_at": 1760292290
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
  "sig": "cb4efda1205a6cdecdb84deba260cf1bbfafbc7f2fac2aff26818005b653adf3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009599036440
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 194, 'threshold': 50, 'total_amount': 77393584, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 193, 'first_seen': 1760285765, 'matching_hash': '93c00e1af0416a0b'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '491975133', 'validation_error': 'Invalid routing number checksum'}}}