```json
{
  "id": "c625b7f19aa39a1a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291503,
  "host_pid": "9e6742732c60:1",
  "hash": "d1505f0f0f4c2df7bbf624abcd52967bc226b4eabef7761005e80b7761ddc918",
  "cid": "QmV1d1505f0f0f4c2df7bbf624abcd52967bc226b4ea",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291503,
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
      "evaluated_at": 1760291503
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
  "sig": "145987a975bb1dba76b04fdd83ec811926a91e61d96f396b8423965bcc3d5012"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000025840854
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 176, 'threshold': 50, 'total_amount': 73943056, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 175, 'first_seen': 1760285765, 'matching_hash': 'de322b9b0535588e'}}}