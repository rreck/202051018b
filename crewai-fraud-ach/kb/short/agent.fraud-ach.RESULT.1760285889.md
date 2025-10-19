```json
{
  "id": "8654a2a2368a6fe9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285889,
  "host_pid": "9e6742732c60:1",
  "hash": "4db8b5ca35b16f98ab65789dbd759692c00ba99bb8205f25bf9252b2717665e8",
  "cid": "QmV14db8b5ca35b16f98ab65789dbd759692c00ba99b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285889,
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
      "evaluated_at": 1760285889
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
  "sig": "452e313255c37e6fac3bece03b0a3c304b072b949d81e2be7c7274bd0b480b5b"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105153776491
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 6, 'first_seen': 1760285763, 'matching_hash': '94746339473c09ed'}}}