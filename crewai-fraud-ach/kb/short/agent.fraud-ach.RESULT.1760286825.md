```json
{
  "id": "dada53534e36f69a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286825,
  "host_pid": "9e6742732c60:1",
  "hash": "c0b42c922690212d1ef64830b271d958192b18d9496803bd605fc0035562ccee",
  "cid": "QmV1c0b42c922690212d1ef64830b271d958192b18d9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286825,
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
      "evaluated_at": 1760286825
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
  "sig": "f5ee4ab8318b234a546908498523f7739e3a795845571a655306890024566a3a"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 12093424, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 37, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}