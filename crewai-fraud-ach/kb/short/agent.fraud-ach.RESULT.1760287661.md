```json
{
  "id": "cccb5a9a74d6c1e3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287661,
  "host_pid": "9e6742732c60:1",
  "hash": "5b8da03413d1674957452a6165ef97a735adfe206779ef00d0cdc501881478d9",
  "cid": "QmV15b8da03413d1674957452a6165ef97a735adfe20",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287661,
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
      "evaluated_at": 1760287661
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
  "sig": "50159acd53a9b7ec935c73d2ad120f877c5d2bbd99e21a5be8788088f60b3d71"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000244875332
Details: {'velocity': {'fraud_detected': True, 'risk_score': 86, 'details': {'transaction_count': 68, 'threshold': 50, 'total_amount': 22314676, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 67, 'first_seen': 1760285763, 'matching_hash': '627c737035c8c8c8'}}}