```json
{
  "id": "c9a8a3cc90120231",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287588,
  "host_pid": "9e6742732c60:1",
  "hash": "1d176fd44dcaf925c03f15039eeeb223af74f6ab5448593945637ec26daad4a7",
  "cid": "QmV11d176fd44dcaf925c03f15039eeeb223af74f6ab",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287588,
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
      "evaluated_at": 1760287588
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
  "sig": "895ce1ba7b248cdd13730905b379959f0146baa3612ee0952438cba9cecc2747"
}
```

Fraud detected: duplicate_transaction (score: 82)
Transaction: 111000021597485
Details: {'velocity': {'fraud_detected': True, 'risk_score': 80, 'details': {'transaction_count': 65, 'threshold': 50, 'total_amount': 17539730, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 64, 'first_seen': 1760285765, 'matching_hash': '53d96e948794c738'}}}