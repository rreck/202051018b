```json
{
  "id": "627d5cf417271791",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286966,
  "host_pid": "9e6742732c60:1",
  "hash": "c4a334777db29c4f6b8820b24f12e4d43ee36fb879c75e61dae74c3e802966b6",
  "cid": "QmV1c4a334777db29c4f6b8820b24f12e4d43ee36fb8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286966,
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
      "evaluated_at": 1760286966
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
  "sig": "c2b4811896cb281620203cc7690c8ffcc884a54d589f7cd452f5b59c3b9c69a3"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105150658717
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 14380404, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 42, 'first_seen': 1760285765, 'matching_hash': 'c0bd022b5af03ee8'}}}