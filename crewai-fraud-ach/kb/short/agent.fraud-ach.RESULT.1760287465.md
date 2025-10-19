```json
{
  "id": "8c98b036abecbe70",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287465,
  "host_pid": "9e6742732c60:1",
  "hash": "6351da12c3c88c130755c99e12f4d8583f688ac574492dddb525376cd3388397",
  "cid": "QmV16351da12c3c88c130755c99e12f4d8583f688ac5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287465,
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
      "evaluated_at": 1760287465
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "e580c3c5793154f03eb1ef499ad7c4861457e2c2686d7bdb25628851f002cff6"
}
```

Fraud detected: duplicate_transaction (score: 78)
Transaction: 021000025260373
Details: {'velocity': {'fraud_detected': True, 'risk_score': 72, 'details': {'transaction_count': 61, 'threshold': 50, 'total_amount': 18960630, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 60, 'first_seen': 1760285765, 'matching_hash': '6c25bdeba85ae9df'}}}