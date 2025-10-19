```json
{
  "id": "a1918d8154ce14db",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291819,
  "host_pid": "9e6742732c60:1",
  "hash": "a7a7350633d3a2d894523203302160738671c13d7603f99b355df7fbb3e8a5fc",
  "cid": "QmV1a7a7350633d3a2d894523203302160738671c13d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291819,
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
      "evaluated_at": 1760291819
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
  "sig": "678c1fb2299ad28c6f7a8ea97a56c8ed72a600c211d8128b87a2a860932e8274"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000027703590
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 184, 'threshold': 50, 'total_amount': 66212952, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 183, 'first_seen': 1760285763, 'matching_hash': '3a097b663e3dde58'}}}