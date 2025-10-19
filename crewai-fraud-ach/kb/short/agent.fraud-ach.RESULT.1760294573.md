```json
{
  "id": "0c80538fc97ca509",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294573,
  "host_pid": "9e6742732c60:1",
  "hash": "6dcc8369c2b8a9761c11eb987b11f23b962281a71f5e863fe118fde9c9c0faa0",
  "cid": "QmV16dcc8369c2b8a9761c11eb987b11f23b962281a7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294573,
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
      "evaluated_at": 1760294573
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
  "sig": "3517b402a3da05d28a3738972ee918539883bc4ba68bada6086762aabd2dd02a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105159928324
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 240, 'threshold': 50, 'total_amount': 105526320, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 239, 'first_seen': 1760285765, 'matching_hash': 'f9e49b53b0020755'}}}