```json
{
  "id": "75f2142d120658a2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286964,
  "host_pid": "9e6742732c60:1",
  "hash": "f049736b9dcfd58641db93e52c2152de863bbd4077f378630efa2499bb1ab962",
  "cid": "QmV1f049736b9dcfd58641db93e52c2152de863bbd40",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286964,
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
      "evaluated_at": 1760286964
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
  "sig": "ee3d49e21b36f20cf47934b4b9420323c4f8fdf28051e2702fc205f755ae2747"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105150676701
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 20242766, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 42, 'first_seen': 1760285765, 'matching_hash': 'f947c72340b5e951'}}}