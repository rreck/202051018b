```json
{
  "id": "fb9b8eee732eeac3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290005,
  "host_pid": "9e6742732c60:1",
  "hash": "85f7221f8e095b6a7ea4e65546e50732600d922333f6df46ddcdce3b7a7d933e",
  "cid": "QmV185f7221f8e095b6a7ea4e65546e50732600d9223",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290005,
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
      "evaluated_at": 1760290005
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
  "sig": "02560768f458f26b7ecdcce967b636e7a12bc101767dcd7543a647ee868e7f2e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000021252160
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 139, 'threshold': 50, 'total_amount': 66163722, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 138, 'first_seen': 1760285763, 'matching_hash': '942f41a705b17558'}}}