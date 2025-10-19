```json
{
  "id": "35476461b3613d28",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290874,
  "host_pid": "9e6742732c60:1",
  "hash": "df530604fb281083e3ec235bddae24ecab69e406630fb527b036d33fb5a1da8d",
  "cid": "QmV1df530604fb281083e3ec235bddae24ecab69e406",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290874,
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
      "evaluated_at": 1760290874
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
  "sig": "763b633e011f22739142fe7b844c36a0128efbdb6ae27ab4035dc550a27d9040"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026725963
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 161, 'threshold': 50, 'total_amount': 32499138, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 160, 'first_seen': 1760285765, 'matching_hash': '729970816697b41b'}}}