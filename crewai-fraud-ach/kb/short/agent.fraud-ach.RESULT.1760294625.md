```json
{
  "id": "98c6b9e87599f1d5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294625,
  "host_pid": "9e6742732c60:1",
  "hash": "b739e17fcfde319f201bf05fb963062bfc76ea1cbad572eaadac3aa44ab38d44",
  "cid": "QmV1b739e17fcfde319f201bf05fb963062bfc76ea1c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294625,
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
      "evaluated_at": 1760294625
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
  "sig": "0544bac9c5311d5c77dd28df09ef7d322efeaff0855dba360bc4d1ad1d7c7dd2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000037652029
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 241, 'threshold': 50, 'total_amount': 68765494, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 240, 'first_seen': 1760285765, 'matching_hash': '6ae01c61248929d6'}}}