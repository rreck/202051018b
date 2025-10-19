```json
{
  "id": "26214ee66d27bfab",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294349,
  "host_pid": "9e6742732c60:1",
  "hash": "6c477a9cdc759598178ee9b65e5676d510fb87fe4a8e487028932e640dc1c8df",
  "cid": "QmV16c477a9cdc759598178ee9b65e5676d510fb87fe",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294349,
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
      "evaluated_at": 1760294349
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
  "sig": "9dbbeac6f539b878e2e000c8d5ceb891427bde7436c414e624f4698855a1ebd9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245772760
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 236, 'threshold': 50, 'total_amount': 15620840, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 235, 'first_seen': 1760285763, 'matching_hash': '6b0c370090b6c980'}}}}