```json
{
  "id": "dc99277062229fb6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290254,
  "host_pid": "9e6742732c60:1",
  "hash": "4dfcbc4c944591500463b8159a8c4299bb5ba3e58e9001bde666d23de4204313",
  "cid": "QmV14dfcbc4c944591500463b8159a8c4299bb5ba3e5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290254,
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
      "evaluated_at": 1760290254
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
  "sig": "ac3c8d483814b97d9594b69ca729f42606c3089609a81499fbf3d92d015481d1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 145, 'threshold': 50, 'total_amount': 46145960, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 144, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}