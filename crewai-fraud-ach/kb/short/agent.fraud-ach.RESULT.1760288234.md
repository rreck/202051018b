```json
{
  "id": "d71c06e4e94626de",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288234,
  "host_pid": "9e6742732c60:1",
  "hash": "20a339975b984fd814a781fb4f420a6ccb82676bb02920576a048afcbee40e16",
  "cid": "QmV120a339975b984fd814a781fb4f420a6ccb82676b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288234,
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
      "evaluated_at": 1760288234
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
  "sig": "8c9223a02a1775a87c1f80093b464ae393940f2e53b13fd6ac8a8e33928b8325"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022356059
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 87, 'threshold': 50, 'total_amount': 14616783, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 86, 'first_seen': 1760285763, 'matching_hash': 'fa8ad4fa6a79b6e4'}}}