```json
{
  "id": "eb701e44bf252b2a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290235,
  "host_pid": "9e6742732c60:1",
  "hash": "12301cc9a34a817d06598b02470c95d17bd644adfc90de449f2b46633d40b982",
  "cid": "QmV112301cc9a34a817d06598b02470c95d17bd644ad",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290235,
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
      "evaluated_at": 1760290235
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
  "sig": "11e35a1be915e00c672034607a45a4a45f6bf9907b60d31211ee3d4b04952e60"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105150369382
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 145, 'threshold': 50, 'total_amount': 51882160, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 144, 'first_seen': 1760285763, 'matching_hash': '1d04175be49b6deb'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '691661790', 'validation_error': 'Invalid routing number checksum'}}}