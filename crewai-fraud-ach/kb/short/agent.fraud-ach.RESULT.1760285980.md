```json
{
  "id": "a202c755433606fa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285980,
  "host_pid": "9e6742732c60:1",
  "hash": "0a9d38265427f6997aa732b84574564c44ddbd12696728fd80c4336cabfad6df",
  "cid": "QmV10a9d38265427f6997aa732b84574564c44ddbd12",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285980,
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
      "evaluated_at": 1760285980
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
  "sig": "d557471aadeba037b4df5bce0d405059ebb6bb40b7d71e84d12ad6aa1d080022"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000021011137
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 9, 'first_seen': 1760285764, 'matching_hash': '3868aeea45d72d6f'}}}