```json
{
  "id": "d658d8a46024336c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287139,
  "host_pid": "9e6742732c60:1",
  "hash": "1f9318cd06c120e9b3c7d1f0c38648d57c9513aa3b41a3bdcf6dacf55f6bc2ba",
  "cid": "QmV11f9318cd06c120e9b3c7d1f0c38648d57c9513aa",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287139,
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
      "evaluated_at": 1760287139
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
  "sig": "85152183ca48b9201b609b8f963e2ce334bf4a17381b70a3c7622968ba992910"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 15594152, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 48, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}