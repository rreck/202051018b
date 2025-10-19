```json
{
  "id": "bd7da975902fce4a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294249,
  "host_pid": "9e6742732c60:1",
  "hash": "f9697282d3ea443ef03099685465b4eb32654df0e9396b049fc0f62dbdca4a74",
  "cid": "QmV1f9697282d3ea443ef03099685465b4eb32654df0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294249,
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
      "evaluated_at": 1760294249
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
  "sig": "7a933cb4ac005354709d2a664e909d7d7783921a17bf8d38c93c5ff161ed91d9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000027918613
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 234, 'threshold': 50, 'total_amount': 26627328, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 233, 'first_seen': 1760285764, 'matching_hash': 'c11d1385920c0a28'}}}