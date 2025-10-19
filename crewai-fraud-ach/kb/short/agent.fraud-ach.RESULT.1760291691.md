```json
{
  "id": "a5aa38ddcc0986e9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291691,
  "host_pid": "9e6742732c60:1",
  "hash": "24126342a0a0ffade09732f8433fba3ee75c6cc2bdbef61e3f731f568e51b696",
  "cid": "QmV124126342a0a0ffade09732f8433fba3ee75c6cc2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291691,
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
      "evaluated_at": 1760291691
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
  "sig": "77d53e78b7652142ee18cab0f58ec103cd3cb834f11c82d334a7a1f5e6a4c0d6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025654087
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 181, 'threshold': 50, 'total_amount': 25302895, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 180, 'first_seen': 1760285763, 'matching_hash': '431eabbdd05dc2b1'}}}