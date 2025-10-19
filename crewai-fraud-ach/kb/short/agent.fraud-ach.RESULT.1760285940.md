```json
{
  "id": "9b7f67b8fc7c841f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285940,
  "host_pid": "9e6742732c60:1",
  "hash": "1df585995726ca4860d79aab211d5d91b3e15d939db13379938479daed7520f0",
  "cid": "QmV11df585995726ca4860d79aab211d5d91b3e15d93",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285940,
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
      "evaluated_at": 1760285940
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
  "sig": "d8b1327792dd9809e5fbefe0384311b43429eddfa48c49ffa4d6721c2482a4d1"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000026044300
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 8, 'first_seen': 1760285763, 'matching_hash': '19d391c08a2c00ab'}}}