```json
{
  "id": "1348677f34dc638a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290613,
  "host_pid": "9e6742732c60:1",
  "hash": "9bd400f75ec4a6b3f19b4dfdec335888760b6a049099266652e88578f984daa8",
  "cid": "QmV19bd400f75ec4a6b3f19b4dfdec335888760b6a04",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290613,
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
      "evaluated_at": 1760290613
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
  "sig": "91631bf84175670f75c14e0a521e9a1125d70848049f4152beaa470a38260e93"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000027962561
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 155, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 154, 'first_seen': 1760285763, 'matching_hash': '3395f05250aaaeda'}}}een': 1760285763, 'matching_hash': '94740eaab516570d'}}}