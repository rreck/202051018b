```json
{
  "id": "43396e2a78779a12",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287242,
  "host_pid": "9e6742732c60:1",
  "hash": "524bdc5d2ed0a8bc9edff3873e85d5d08c582f5a0f3478021dd1e1c13cad4594",
  "cid": "QmV1524bdc5d2ed0a8bc9edff3873e85d5d08c582f5a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287242,
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
      "evaluated_at": 1760287242
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "8c47bc8f4d5bd1dcce9ecf859fa3e831de4ac56c07a8167f87937aeaf00fe7ea"
}
```

Fraud detected: duplicate_transaction (score: 70)
Transaction: 031201467867880
Details: {'velocity': {'fraud_detected': True, 'risk_score': 56, 'details': {'transaction_count': 53, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 52, 'first_seen': 1760285765, 'matching_hash': 'd47cb9c035f50d52'}}}een': 1760285763, 'matching_hash': 'efb59c040be3d116'}}}