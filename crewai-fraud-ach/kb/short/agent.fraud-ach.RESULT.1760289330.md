```json
{
  "id": "5404deba08369e43",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289330,
  "host_pid": "9e6742732c60:1",
  "hash": "63e9b9924651294cba1a0e087dcf97bcdac0a79542a676cfff8e1b74a2410d1a",
  "cid": "QmV163e9b9924651294cba1a0e087dcf97bcdac0a795",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289330,
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
      "evaluated_at": 1760289330
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
  "sig": "db02a8a5d830aff618d2703d33baed50c97520ab000b0cb13ccc6f5b350b7b86"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000027783214
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 196, 'threshold': 50, 'total_amount': 95095476, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 195, 'first_seen': 1760284979, 'matching_hash': '00d004b11e9e3015'}}}