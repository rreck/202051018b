```json
{
  "id": "951eb056df4fdf62",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289724,
  "host_pid": "9e6742732c60:1",
  "hash": "f9bdfa1f8e15804bd79347b4a62662f7e012daf649e5e2cbd6e9f8d990517e99",
  "cid": "QmV1f9bdfa1f8e15804bd79347b4a62662f7e012daf6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289724,
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
      "evaluated_at": 1760289724
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
  "sig": "589a580cd8fadfb6b4f7472dba0ad031fde19849e081a23cd1689cde889c7f4f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000038959082
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 131, 'threshold': 50, 'total_amount': 11276349, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 130, 'first_seen': 1760285765, 'matching_hash': '98ae9ae4174799d3'}}}