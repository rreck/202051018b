```json
{
  "id": "9537b2e28ba6452a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288411,
  "host_pid": "9e6742732c60:1",
  "hash": "6240ac4134b71413cfb02e247ecd94b1cf5bac0beb745b79dad14d18231cc5d4",
  "cid": "QmV16240ac4134b71413cfb02e247ecd94b1cf5bac0b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288411,
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
      "evaluated_at": 1760288411
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
  "sig": "3c04b5862a5aea5554c102bc342b0b663b52ada26028afc227e4270eb05aeb67"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000249254910
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 92, 'threshold': 50, 'total_amount': 10506216, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 91, 'first_seen': 1760285765, 'matching_hash': '80dc97a16e454830'}}}