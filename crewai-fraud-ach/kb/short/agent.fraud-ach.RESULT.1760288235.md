```json
{
  "id": "d3100b3728cbee31",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288235,
  "host_pid": "9e6742732c60:1",
  "hash": "710bcde66527e1b3fb5b0a80438ea3915ac288eadbe420e34c5ba1032731a54d",
  "cid": "QmV1710bcde66527e1b3fb5b0a80438ea3915ac288ea",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288235,
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
      "evaluated_at": 1760288235
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
  "sig": "11a1b03d6f387c3ec54ad8380fcf9f27bcd27c6c212781bdf1522e55b4f28cb6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000029379143
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 87, 'threshold': 50, 'total_amount': 42345510, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 86, 'first_seen': 1760285763, 'matching_hash': '781972e95177ec49'}}}