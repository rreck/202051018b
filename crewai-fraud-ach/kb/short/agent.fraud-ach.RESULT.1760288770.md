```json
{
  "id": "eba8d92b7a5bc5ef",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288770,
  "host_pid": "9e6742732c60:1",
  "hash": "e4a35d5fac597541237bfbd10159019b7d3d608801be1e04526f2082927c54ea",
  "cid": "QmV1e4a35d5fac597541237bfbd10159019b7d3d6088",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288770,
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
      "evaluated_at": 1760288770
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
  "sig": "3b9a3a22d9a8030a74a69a1e63a9c6e510d08d00790cfb8cd5529d130ff022ce"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021480535
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 103, 'threshold': 50, 'total_amount': 50804441, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 102, 'first_seen': 1760285765, 'matching_hash': '9682be52dcbb3d1d'}}}