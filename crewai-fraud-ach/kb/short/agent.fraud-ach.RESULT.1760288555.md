```json
{
  "id": "a14281987823fc87",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288555,
  "host_pid": "9e6742732c60:1",
  "hash": "782e12e43b80d89b88d4faf934e5e016f4a6a44559a931df465167446f721501",
  "cid": "QmV1782e12e43b80d89b88d4faf934e5e016f4a6a445",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288555,
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
      "evaluated_at": 1760288555
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
  "sig": "f562729c05d1fda029fbbfdaad833f2dba86238c82b139ad4ecc83e3938fa9bb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201463967385
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 97, 'threshold': 50, 'total_amount': 35032617, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 96, 'first_seen': 1760285763, 'matching_hash': 'becd1833b82f29ed'}}}