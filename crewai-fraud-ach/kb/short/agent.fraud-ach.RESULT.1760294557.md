```json
{
  "id": "273466db80958d91",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294557,
  "host_pid": "9e6742732c60:1",
  "hash": "f81f07fddc44a7ce5b7c4bb368720d40391ba9ef2627f16532437e74bd553029",
  "cid": "QmV1f81f07fddc44a7ce5b7c4bb368720d40391ba9ef",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294557,
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
      "evaluated_at": 1760294557
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
  "sig": "b961959b887904e14d00d99e80cbf3f22333d14dc09e055a2a3b25bf6c3dadfd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464924143
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 316, 'threshold': 50, 'total_amount': 128417660, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 315, 'first_seen': 1760284979, 'matching_hash': '7b94effc1b7c4489'}}}