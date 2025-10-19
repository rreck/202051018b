```json
{
  "id": "c3162ce713b29767",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293168,
  "host_pid": "9e6742732c60:1",
  "hash": "f39f0710965e64c4a688f093a05325836af85ed3c5761a4fe3a83573775f527a",
  "cid": "QmV1f39f0710965e64c4a688f093a05325836af85ed3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293168,
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
      "evaluated_at": 1760293168
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
  "sig": "ebd8f1ab5600e663542f5eb6f13d87e457f9e161a013c2d089a8d7332b884283"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000024298856
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 213, 'threshold': 50, 'total_amount': 72694770, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 212, 'first_seen': 1760285763, 'matching_hash': 'c651031c314af1fc'}}}}'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '472304300', 'validation_error': 'Invalid routing number checksum'}}}