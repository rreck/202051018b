```json
{
  "id": "77d1894f5e0e2c18",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291934,
  "host_pid": "9e6742732c60:1",
  "hash": "d155154795a8423d92c3ad6dcb665fdfe98e2b854b020ce369689c69d4ace8a0",
  "cid": "QmV1d155154795a8423d92c3ad6dcb665fdfe98e2b85",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291934,
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
      "evaluated_at": 1760291934
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
  "sig": "2082ef12d6945c51f842edb19f212566583ad456744a89acb36cbc99de9ecea1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000022109746
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 186, 'threshold': 50, 'total_amount': 22418394, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 185, 'first_seen': 1760285765, 'matching_hash': '2a578690bb80e431'}}}