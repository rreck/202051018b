```json
{
  "id": "1bc86ae1c0c480fe",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290700,
  "host_pid": "9e6742732c60:1",
  "hash": "f3fdf39ada2ca82938ca0dac98ed7fbb48591ece0517d5c0f72c0e0bee72680c",
  "cid": "QmV1f3fdf39ada2ca82938ca0dac98ed7fbb48591ece",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290700,
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
      "evaluated_at": 1760290700
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
  "sig": "9055411daab61f806aae205fa71ee52fe462e123b5062726a8f339a106e50245"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105150592686
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 157, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 156, 'first_seen': 1760285763, 'matching_hash': '43d52159a9989a8b'}}}5763, 'matching_hash': '0cc689f8838aa314'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '113877666', 'validation_error': 'Invalid routing number checksum'}}}