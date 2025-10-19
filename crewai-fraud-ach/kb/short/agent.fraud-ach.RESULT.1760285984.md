```json
{
  "id": "c819d8280f0afb24",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285984,
  "host_pid": "9e6742732c60:1",
  "hash": "7a17bfee50dec0b082709384c898368eeb0e90215d561d09542066f15eb4a852",
  "cid": "QmV17a17bfee50dec0b082709384c898368eeb0e9021",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285984,
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
      "evaluated_at": 1760285984
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
  "sig": "1e625941509958d44cf7ee3e864bf343d8cacb52f7a532fa9e59fa12f61092f6"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000021513577
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 9, 'first_seen': 1760285765, 'matching_hash': '2d9e7d16ad0b5ba4'}}}