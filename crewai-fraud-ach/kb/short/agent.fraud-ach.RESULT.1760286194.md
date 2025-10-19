```json
{
  "id": "2a445c5b54b4aa01",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286194,
  "host_pid": "9e6742732c60:1",
  "hash": "5d087f2919d2faff7f544efb38296a15c0a681acf4d768ff0dabb113ceaa536e",
  "cid": "QmV15d087f2919d2faff7f544efb38296a15c0a681ac",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286194,
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
      "evaluated_at": 1760286194
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
  "sig": "6c1ae0079cd0d581f45effd2d6dafb2a3d361e9eee97150b62a9c40e9c37cb99"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105153539871
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 16, 'first_seen': 1760285765, 'matching_hash': '6120bfc166994b37'}}}