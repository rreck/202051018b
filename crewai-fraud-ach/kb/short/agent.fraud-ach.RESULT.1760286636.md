```json
{
  "id": "890dc7d80b0857be",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286636,
  "host_pid": "9e6742732c60:1",
  "hash": "a34cf37436994855f230d11019dba9873131e69701e9507a3dc2b7fd395e94fe",
  "cid": "QmV1a34cf37436994855f230d11019dba9873131e697",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286636,
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
      "evaluated_at": 1760286636
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
  "sig": "cee5c01fb9a4a6782943fe78fd94a748ef17c5e160e36760238df945537e4094"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000029303857
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 31, 'first_seen': 1760285763, 'matching_hash': '4510d576292a5401'}}}