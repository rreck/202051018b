```json
{
  "id": "1b1c4ddffb83b081",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288785,
  "host_pid": "9e6742732c60:1",
  "hash": "902d17edd1ea4ed569ef229e8f570f45689af0a8bb5968ec1546091a65477ed7",
  "cid": "QmV1902d17edd1ea4ed569ef229e8f570f45689af0a8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288785,
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
      "evaluated_at": 1760288785
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
  "sig": "9c574736d02f6f213249eddacbe5c47372d44b62bfb01c09cae68c2ae71b044c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009595770141
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 104, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 103, 'first_seen': 1760285763, 'matching_hash': '07c751792fcc9457'}}}een': 1760285763, 'matching_hash': 'c651031c314af1fc'}}}