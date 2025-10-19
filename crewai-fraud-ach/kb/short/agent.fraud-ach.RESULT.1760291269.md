```json
{
  "id": "368ebff09e380b2b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291269,
  "host_pid": "9e6742732c60:1",
  "hash": "4f087c732a09794e82ea0347c27e9314d9047fa9c890519dd6ec974ccdcc6e23",
  "cid": "QmV14f087c732a09794e82ea0347c27e9314d9047fa9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291269,
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
      "evaluated_at": 1760291269
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
  "sig": "11668c2b6ddd353cfcfcab98a6db09b995bcf9149da766f96ece3be22541042a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241330040
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 171, 'threshold': 50, 'total_amount': 45583470, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 170, 'first_seen': 1760285763, 'matching_hash': '556aef048193b362'}}}