```json
{
  "id": "5ddbb981b7633f78",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286131,
  "host_pid": "9e6742732c60:1",
  "hash": "1a06268ed7995c550e12e2dd3fb7ec683bdc810e4cf4e02a4b7ec2129fe72de7",
  "cid": "QmV11a06268ed7995c550e12e2dd3fb7ec683bdc810e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286131,
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
      "evaluated_at": 1760286131
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
  "sig": "9ac90f6dd4b2247ccae6f5f0ac58beba2af210adf217cb335f8dc09142cc596f"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000025883497
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 14, 'first_seen': 1760285765, 'matching_hash': '8c29ee71720a2634'}}}