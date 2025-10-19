```json
{
  "id": "92547a6a40dd270d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286614,
  "host_pid": "9e6742732c60:1",
  "hash": "b5c0af171a38cc0f4d6599ff4a0c91b43cf09400af8b97207b197dc2eef30720",
  "cid": "QmV1b5c0af171a38cc0f4d6599ff4a0c91b43cf09400",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286614,
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
      "evaluated_at": 1760286614
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
  "sig": "11d94d28748ea53b619e365adc706e40614efcfaf066111b63d9cf36f380ff45"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000241083307
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 30, 'first_seen': 1760285763, 'matching_hash': '06ddfe971a6a4d24'}}}