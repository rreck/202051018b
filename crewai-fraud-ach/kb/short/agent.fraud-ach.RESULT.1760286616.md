```json
{
  "id": "c60004a1178cec54",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286616,
  "host_pid": "9e6742732c60:1",
  "hash": "acd3e4c753710ca3b7dd6bb54eb087e3d45bf15bd481d0e40334bc4ec9317cae",
  "cid": "QmV1acd3e4c753710ca3b7dd6bb54eb087e3d45bf15b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286616,
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
      "evaluated_at": 1760286616
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
  "sig": "46ff29fac4c3546a56e015ab74e4fac33549fefc37c105a4e7bafd1276fb4ef0"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 031201468417432
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 10530948, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 30, 'first_seen': 1760285764, 'matching_hash': '3485380f8c896007'}}}