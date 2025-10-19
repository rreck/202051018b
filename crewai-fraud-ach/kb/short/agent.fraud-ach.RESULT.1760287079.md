```json
{
  "id": "1c8dc9669f52e032",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287079,
  "host_pid": "9e6742732c60:1",
  "hash": "e662275bdb228265cf68c33c3e844622b36397622e62163a264a601a584dca1a",
  "cid": "QmV1e662275bdb228265cf68c33c3e844622b3639762",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287079,
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
      "evaluated_at": 1760287079
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
  "sig": "5a4cba6a0d93dcf35825f38c19d141eeb30974f894908e0e21e159877ecf206b"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 026009597862857
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 46, 'first_seen': 1760285765, 'matching_hash': 'eac3ff1003c03af8'}}}