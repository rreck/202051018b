```json
{
  "id": "2a1f1a5ad0730f4a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291936,
  "host_pid": "9e6742732c60:1",
  "hash": "4ac4c0de18fb8c402ed93c824ddeaf0c4bedcd3c262ad34c73bd04aa8f004be5",
  "cid": "QmV14ac4c0de18fb8c402ed93c824ddeaf0c4bedcd3c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291936,
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
      "evaluated_at": 1760291936
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
  "sig": "5500f776c0ba87bed292a57e5dc5bf60382d33329823671a406d3c18ae25db49"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009597862857
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 186, 'threshold': 50, 'total_amount': 37166892, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 185, 'first_seen': 1760285765, 'matching_hash': 'eac3ff1003c03af8'}}}