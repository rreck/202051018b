```json
{
  "id": "edaf92556fb78e70",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286672,
  "host_pid": "9e6742732c60:1",
  "hash": "a44c7d42dbbc16803c3e04a5742fd3702c3aec1d6aaa162ad1e2fb13157aae53",
  "cid": "QmV1a44c7d42dbbc16803c3e04a5742fd3702c3aec1d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286672,
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
      "evaluated_at": 1760286672
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
  "sig": "dba319182240f8473f94f5585893ec0ffd0f4b54f66b21816975ac0a86b7497a"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000244410720
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 32, 'first_seen': 1760285763, 'matching_hash': 'eab520de73a5b8cf'}}}