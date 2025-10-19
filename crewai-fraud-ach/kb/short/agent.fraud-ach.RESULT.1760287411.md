```json
{
  "id": "1105e31d16b0e2fd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287411,
  "host_pid": "9e6742732c60:1",
  "hash": "7b4a29b1469a1d2baa96fa6f89a2530653e303a3f88bc84c4f952ab84268c7d9",
  "cid": "QmV17b4a29b1469a1d2baa96fa6f89a2530653e303a3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287411,
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
      "evaluated_at": 1760287411
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "invalid_routing",
    "risk_critical"
  ],
  "sig": "0320018ca201d3e074d3c9e36805bbe291f7ce5c78b43bc0707604997626a8ac"
}
```

Fraud detected: invalid_routing (score: 83)
Transaction: 789209528183836
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 59, 'threshold': 50, 'total_amount': 15384073, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 58, 'first_seen': 1760285765, 'matching_hash': 'e8f44f77b3005867'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '789209527', 'validation_error': 'Invalid routing number checksum'}}}