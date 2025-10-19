```json
{
  "id": "a29d58d3c7bb157b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293239,
  "host_pid": "9e6742732c60:1",
  "hash": "78e6fad4effed0bf479a756a3208a10b797a3ee4f84c4aa7d9d1a21050c77cac",
  "cid": "QmV178e6fad4effed0bf479a756a3208a10b797a3ee4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293239,
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
      "evaluated_at": 1760293239
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
  "sig": "2c40a31534f22d5ae16b0ad931954414c6f8f9af863a0241e6915c10db9e36eb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201468417432
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 214, 'threshold': 50, 'total_amount': 72697512, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 213, 'first_seen': 1760285764, 'matching_hash': '3485380f8c896007'}}}