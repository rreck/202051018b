```json
{
  "id": "116293a3f6642ace",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288692,
  "host_pid": "9e6742732c60:1",
  "hash": "00a7315a347c2bd0bb77294ef352aff6c696543bb43752799492b4a3b90a7a2c",
  "cid": "QmV100a7315a347c2bd0bb77294ef352aff6c696543b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288692,
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
      "evaluated_at": 1760288692
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
  "sig": "596c09e4c1fd49ac03b4dd3876ad3e748c3fa7abe5c51738257c61dbbcabbf10"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000031758687
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 101, 'threshold': 50, 'total_amount': 40780972, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 100, 'first_seen': 1760285763, 'matching_hash': '8a33e153fff23185'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '834096558', 'validation_error': 'Invalid routing number checksum'}}}