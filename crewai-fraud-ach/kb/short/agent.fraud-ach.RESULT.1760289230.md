```json
{
  "id": "249138470cb587e4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289230,
  "host_pid": "9e6742732c60:1",
  "hash": "1596f152112e589178508b246d492b38e8ac48a2177e2ed1c4fbbedcb981ee47",
  "cid": "QmV11596f152112e589178508b246d492b38e8ac48a2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289230,
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
      "evaluated_at": 1760289230
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
  "sig": "e5fd07ce87ffbba8e7dd9c9922898c882ba26b9728e9b5af07bbbb4fc6d38bb3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105158219859
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 117, 'threshold': 50, 'total_amount': 49557573, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 116, 'first_seen': 1760285765, 'matching_hash': '5fa0c304c44ad0bf'}}}