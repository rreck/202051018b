```json
{
  "id": "a63162bf72b66d13",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290510,
  "host_pid": "9e6742732c60:1",
  "hash": "bed2ca9d643e04c91417a143f0061c6af2ff9b78bdb19efd84b35e3825782462",
  "cid": "QmV1bed2ca9d643e04c91417a143f0061c6af2ff9b78",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290510,
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
      "evaluated_at": 1760290510
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
  "sig": "d7538c2a2d1556b400eac4149c15b2a15dc5df5e0fa1d8daadb10c6e0c9ce9e6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105152729668
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 152, 'threshold': 50, 'total_amount': 21317392, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 151, 'first_seen': 1760285763, 'matching_hash': 'e33e77be4df2721a'}}}