```json
{
  "id": "409c59b6d82de286",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291361,
  "host_pid": "9e6742732c60:1",
  "hash": "c6b321b967748e27b159a001401d7a2f278a90cd29ddbb3092ed230d3c597a19",
  "cid": "QmV1c6b321b967748e27b159a001401d7a2f278a90cd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291361,
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
      "evaluated_at": 1760291361
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
  "sig": "d7682187853c326d5620122c46f9038e7a791535ae455470cab74156774327aa"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245112669
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 173, 'threshold': 50, 'total_amount': 13942243, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 172, 'first_seen': 1760285764, 'matching_hash': '067804ada8f7cd8c'}}}