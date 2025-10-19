```json
{
  "id": "d44d7a292ea5ab2b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294416,
  "host_pid": "9e6742732c60:1",
  "hash": "a06915c870717ee29086ae6044c4e29c616702556d2cce33301e7b974ae4691a",
  "cid": "QmV1a06915c870717ee29086ae6044c4e29c61670255",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294416,
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
      "evaluated_at": 1760294416
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
  "sig": "21bd595de3a91d1b60e9f5227c976882ab3300df1c23fa5c9cc7c3d1fe75c2c3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 237, 'threshold': 50, 'total_amount': 75424776, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 236, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}