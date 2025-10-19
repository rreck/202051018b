```json
{
  "id": "774db49d8be36309",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291645,
  "host_pid": "9e6742732c60:1",
  "hash": "a24347719c04b830cccead8c72dcf16f586a02f76d193d2cc6bc3b39a73257b3",
  "cid": "QmV1a24347719c04b830cccead8c72dcf16f586a02f7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291645,
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
      "evaluated_at": 1760291645
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
  "sig": "48589a5232df7bdfa9bdd02a74e1e8ad652a7f2d08d162956333a578b1053688"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464951398
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 180, 'threshold': 50, 'total_amount': 48612780, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 179, 'first_seen': 1760285763, 'matching_hash': '40dace0dcec07d54'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '580123066', 'validation_error': 'Invalid routing number checksum'}}}