```json
{
  "id": "81e7da0f5924b6f7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287955,
  "host_pid": "9e6742732c60:1",
  "hash": "768e183d5f9a6185fd9e2038ce2dba31f97f42ed3eb8e5c877d97d4035a82370",
  "cid": "QmV1768e183d5f9a6185fd9e2038ce2dba31f97f42ed",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287955,
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
      "evaluated_at": 1760287955
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
  "sig": "8b868ee190757dba046b4afefe0502c3d1a52d7859553665c490c9c5e201f348"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000036798243
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 78, 'threshold': 50, 'total_amount': 34483176, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 77, 'first_seen': 1760285763, 'matching_hash': '9f3869b775bbb8aa'}}}