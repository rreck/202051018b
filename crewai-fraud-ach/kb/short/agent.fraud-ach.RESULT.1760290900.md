```json
{
  "id": "416732a7c5087c6a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290900,
  "host_pid": "9e6742732c60:1",
  "hash": "72da76ab0a95c53507fac914626c3fce13a3c0ade732869dcd5cf073560bd6e9",
  "cid": "QmV172da76ab0a95c53507fac914626c3fce13a3c0ad",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290900,
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
      "evaluated_at": 1760290900
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
  "sig": "92598982f9fd24f2a64ae74bd5b24bd984f8303815008209db104970d4601f6c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100276179264
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 162, 'threshold': 50, 'total_amount': 27775872, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 161, 'first_seen': 1760285763, 'matching_hash': 'cb2614db0e970d70'}}}