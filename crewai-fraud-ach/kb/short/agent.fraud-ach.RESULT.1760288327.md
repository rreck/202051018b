```json
{
  "id": "86b53d76070867a1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288327,
  "host_pid": "9e6742732c60:1",
  "hash": "ae9a8876c796598f8bd744fb52d43b7970a696ed1933b2e0f5a50f6b5fb060cb",
  "cid": "QmV1ae9a8876c796598f8bd744fb52d43b7970a696ed",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288327,
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
      "evaluated_at": 1760288327
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
  "sig": "8423fa9a3bdee227ff27db74ede042031d77afbf164e0fe35e8041d05fbb8cee"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201467455813
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 90, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 89, 'first_seen': 1760285763, 'matching_hash': 'dd25b8ab6718ff18'}}}een': 1760285763, 'matching_hash': 'c482c58c8f3e1991'}}}