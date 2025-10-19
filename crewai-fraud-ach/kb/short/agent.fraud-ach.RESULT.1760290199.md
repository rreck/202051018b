```json
{
  "id": "e2c5d6200cf61d23",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290199,
  "host_pid": "9e6742732c60:1",
  "hash": "5e3e1e1d17e3390bce0361e2e8e080eb595eca2ba1d74c0b0eb1899575870e3f",
  "cid": "QmV15e3e1e1d17e3390bce0361e2e8e080eb595eca2b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290199,
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
      "evaluated_at": 1760290199
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
  "sig": "b065ddb36fed259ac3135bb8e07f15d18b82780d91c5ca4a33bf6b92c7191491"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105152772165
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 144, 'threshold': 50, 'total_amount': 41847264, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 143, 'first_seen': 1760285764, 'matching_hash': '9371db7725d4e0a9'}}}