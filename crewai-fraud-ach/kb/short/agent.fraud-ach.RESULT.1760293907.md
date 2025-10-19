```json
{
  "id": "a6450f80de66fa93",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293907,
  "host_pid": "9e6742732c60:1",
  "hash": "88c62260a6a19f008129de900aa799071b947f7a263571891aade4dfedd8e095",
  "cid": "QmV188c62260a6a19f008129de900aa799071b947f7a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293907,
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
      "evaluated_at": 1760293907
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
  "sig": "ab49eccf67420a2892228aec6c26253319cbc4bf2ee0a323396a1b34f4fce37c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271295485
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 228, 'threshold': 50, 'total_amount': 86960568, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 227, 'first_seen': 1760285763, 'matching_hash': '1c5bb12c0a4cbea7'}}}