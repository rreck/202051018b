```json
{
  "id": "a47b0b8109fca8d7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293639,
  "host_pid": "9e6742732c60:1",
  "hash": "fd37704b638aaba318b21abc98005b4ce0906e62bfafb8b094f44b14551cd262",
  "cid": "QmV1fd37704b638aaba318b21abc98005b4ce0906e62",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293639,
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
      "evaluated_at": 1760293639
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
  "sig": "2ffd0045844d56e9355e5f06fc74fb6f7f54101ac2716dca8ac2d4dd7030bfd0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 222, 'threshold': 50, 'total_amount': 70651056, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 221, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}