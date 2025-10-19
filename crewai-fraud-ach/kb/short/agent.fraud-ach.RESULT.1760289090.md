```json
{
  "id": "e5a1775dbb66be0a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289090,
  "host_pid": "9e6742732c60:1",
  "hash": "eb2ad6f07ce434d9c2ba2c99d7fb541a7fd05ecda3bcd2ea43d425796d6c1d48",
  "cid": "QmV1eb2ad6f07ce434d9c2ba2c99d7fb541a7fd05ecd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289090,
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
      "evaluated_at": 1760289090
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
  "sig": "166fdb9c89c85d7c9d09c1b73b0d61a4d6563881f94de778598857994bf13fd8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154261308
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 113, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 112, 'first_seen': 1760285763, 'matching_hash': 'f5aec8f7458ab0e7'}}}een': 1760285764, 'matching_hash': '998be1a53ec99162'}}}