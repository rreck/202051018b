```json
{
  "id": "2e0feb2d885906f9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289494,
  "host_pid": "9e6742732c60:1",
  "hash": "a5c5214ce444c5c211db43ed5e591db4795ebaef54a38d5c44d5d97b1a4b2c0e",
  "cid": "QmV1a5c5214ce444c5c211db43ed5e591db4795ebaef",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289494,
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
      "evaluated_at": 1760289494
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
  "sig": "3439329f6dfd401b4ea1f95791080a0219941a02edb059163c1c8a7320384e96"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025444978
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 125, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 124, 'first_seen': 1760285763, 'matching_hash': 'f3568a0597cdbf93'}}}5763, 'matching_hash': '4a74fde2b8c56926'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '987899137', 'validation_error': 'Invalid routing number checksum'}}}