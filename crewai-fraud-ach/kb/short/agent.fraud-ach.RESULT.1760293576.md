```json
{
  "id": "5fddb4396aafa954",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293576,
  "host_pid": "9e6742732c60:1",
  "hash": "0f12faaa684f00a2c4d11c1eed55ba4ab528551d1b56c5ab8a4ddb1697aa44a7",
  "cid": "QmV10f12faaa684f00a2c4d11c1eed55ba4ab528551d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293576,
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
      "evaluated_at": 1760293576
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
  "sig": "701ee0790e3e2323e8a8911ac7a8e7c336ff3e11454fa36e26d895219035cc40"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026451752
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 297, 'threshold': 50, 'total_amount': 73265148, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 296, 'first_seen': 1760284979, 'matching_hash': 'ed66d17e763eb837'}}}